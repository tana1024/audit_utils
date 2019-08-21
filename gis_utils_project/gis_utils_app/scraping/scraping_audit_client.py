import requests
import re
import sqlite3
import sys
import argparse
import smtplib
from bs4 import BeautifulSoup
from django.db import models
from contextlib import closing
from email.mime.text import MIMEText


class ScrapingAuditClientExecutor:

    SIGHT_URL = 'https://上場企業サーチ.com/'

    AUDIT_CODE_DICT = {
        'sn': {
            'name': '新日本監査法人',
            'client_url': 'analyses/auditor_clients/ＥＹ新日本有限責任監査法人?page='
        },
        'az': {
            'name': 'あずさ監査法人',
            'client_url': 'analyses/auditor_clients/有限責任あずさ監査法人?page='
        },
        'dt': {
            'name': 'デロイトトーマツ監査法人',
            'client_url': 'analyses/auditor_clients/有限責任監査法人トーマツ?page='
        },
        'ar': {
            'name': 'あらた監査法人',
            'client_url': 'analyses/auditor_clients/ＰｗＣあらた有限責任監査法人?page='
        }
    }
    message = "%sのクライアント情報の更新が完了しました。/n" + \
              "更新件数: %d"
    audit_code = 'sn'
    PAGE_LIMIT = 3
    count = 0

    def pre_scraping(self):
        with closing(sqlite3.connect('/workspace/gis_utils/gis_utils_project/db.sqlite3')) as conn:
            # pylint: disable=E1101
            c = conn.cursor()
            c.execute('delete from gis_utils_app_client where audit_code = ' + "'" + self.audit_code + "'")
            conn.commit()
            conn.close()

    def post_scraping(self):
        print('クライアント情報更新の通知処理開始')

        # MIMEの作成
        subject = "クライアント情報更新の完了通知"
        self.message = self.message % (self.AUDIT_CODE_DICT[self.audit_code]['name'], self.count)
        msg = MIMEText(self.message, 'plain')
        msg["Subject"] = subject
        msg["To"] = 'tana2dev1@gmail.com'
        msg["From"] = 'tana2dev3@gmail.com'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('tana2dev3@gmail.com', 'heroku2!git')
        server.send_message(msg)
        server.quit()

        print('クライアント情報更新の通知処理終了')

    def scraping(self):
        print('クライアント情報更新開始')

        for i in range(self.PAGE_LIMIT):
            response = requests.get(self.SIGHT_URL + self.AUDIT_CODE_DICT[self.audit_code]['client_url'] + str(i+1))
            # pylint: disable=E1101
            if response.status_code != requests.codes.ok:
                print('担当企業一覧ページがありません。')
                return
            soup = BeautifulSoup(response.content, 'html.parser')
            a_list = soup.find_all('a', href=re.compile('.*/companies/.*'))
            h_list = list(map(lambda x: x['href'], a_list))

            models = []
            for h in h_list:
                response = requests.get(self.SIGHT_URL + h)
                if response.status_code != requests.codes.ok:
                    print('担当企業詳細ページがありません。')
                    continue
                soup = BeautifulSoup(response.content, "html.parser")
                model = (
                    soup.find('h2').contents[0].strip().split(' ')[0],
                    soup.find('h2').contents[0].strip().split(' ')[1].replace('\u3000', ' '),
                    soup.find(id='address2').find('a').contents[0].strip()[9:] if len(soup.find(id='address2').find('a').contents) != 0 else 'N/A',
                    self.audit_code
                )
                models.append(model)
                print(model)
                self.count = self.count + 1

            self.insert(models)

        print('クライアント情報更新完了')

    def insert(self, models):
        with closing(sqlite3.connect('/workspace/gis_utils/gis_utils_project/db.sqlite3')) as conn:
            # pylint: disable=E1101
            c = conn.cursor()
            insert_sql = 'replace into gis_utils_app_client (s_code, name, street_address, audit_code) values (?,?,?,?)'
            c.executemany(insert_sql, models)
            conn.commit()
            conn.close()

    def __init__(self, audit_code):
        self.audit_code = audit_code


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('audit_code')

    args = parser.parse_args()

    exec = ScrapingAuditClientExecutor(args.audit_code)
    exec.pre_scraping()
    exec.scraping()
    exec.post_scraping()

import requests
import re
import sqlite3
import sys
import argparse
from bs4 import BeautifulSoup
from django.db import models
from contextlib import closing


class ScrapingAuditClientExecutor:

    SIGHT_URL = 'https://上場企業サーチ.com/'
    PAGE_CLIENT_DICT = {
        'sn': 'analyses/auditor_clients/ＥＹ新日本有限責任監査法人?page=',
        'az': 'analyses/auditor_clients/有限責任あずさ監査法人?page=',
        'dt': 'analyses/auditor_clients/有限責任監査法人トーマツ?page=',
        'ar': 'analyses/auditor_clients/ＰｗＣあらた有限責任監査法人?page='
    }
    audit_code = 'sn'

    def pre_scraping(self):
        with closing(sqlite3.connect('/workspace/gis_utils/gis_utils_project/db.sqlite3')) as conn:
            # pylint: disable=E1101
            c = conn.cursor()
            c.execute('delete from gis_utils_app_client where audit_code = ' + "'" + self.audit_code + "'")
            conn.commit()
            conn.close()

    def scraping(self):

        for i in range(100):
            response = requests.get(self.SIGHT_URL + self.PAGE_CLIENT_DICT[self.audit_code] + str(i+1))
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

            self.insert(models)

    def insert(self, models):
        with closing(sqlite3.connect('/workspace/gis_utils/gis_utils_project/db.sqlite3')) as conn:
            # pylint: disable=E1101
            c = conn.cursor()
            insert_sql = 'insert into gis_utils_app_client (s_code, name, street_address, audit_code) values (?,?,?,?)'
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

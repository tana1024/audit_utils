import os
import sys
import time
import requests
import re
import sqlite3
import argparse
import smtplib
import xml.etree.ElementTree as etree
from decimal import Decimal
from datetime import datetime
from pytz import timezone
from bs4 import BeautifulSoup
from contextlib import closing
from email.mime.text import MIMEText

from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker, scoped_session
from sqlalchemy.ext.automap import automap_base

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
    GEOCODING_API_URL = 'https://www.geocoding.jp/api/'
    PAGE_LIMIT = 5
    STATUS_PROGRESS = '1'
    STATUS_COMPLETE = '2'

    message = "%sのクライアント情報の更新が完了しました。\n" + \
              "更新件数: %d"
    audit_code = 'sn'  # default value is 'sn'
    count = 0
    base = None
    session = None


    def pre_scraping(self):
        table = base.classes.gis_utils_app_clientupdatestatus
        self.session.query(table).filter(table.audit_code==self.audit_code).delete()
        self.session.add(table(audit_code=self.audit_code, status=self.STATUS_PROGRESS, update_count=None, update_datetime=datetime.now(timezone('UTC'))))
        table = base.classes.gis_utils_app_client
        self.session.query(table).filter(table.audit_code==self.audit_code).delete()

    def post_scraping(self):
        print('クライアント情報更新の通知処理開始')

        table = base.classes.gis_utils_app_clientupdatestatus
        model = self.session.query(table).filter(table.audit_code==self.audit_code).first()
        model.status = self.STATUS_COMPLETE
        model.update_count = self.count
        model.update_datetime = datetime.now(timezone('UTC'))

        # MIMEの作成
        subject = "クライアント情報更新の完了通知"
        self.message = self.message % (self.AUDIT_CODE_DICT[self.audit_code]['name'], self.count)
        msg = MIMEText(self.message, 'plain')
        msg["Subject"] = subject
        msg["To"] = 'gisutilsdev1@cock.li'  # 値を設定すること
        msg["From"] = 'gisutilsdev3@cock.li'  # 値を設定すること

        server = smtplib.SMTP('mail.cock.li', 587)  # 値を設定すること
        server.starttls()
        server.login('gisutilsdev3@cock.li', 'odxf7lgm')  # 値を設定すること
        server.send_message(msg)
        server.quit()

    #     print('クライアント情報更新の通知処理終了')

    def adjust_scale(self, soup, target):
        unit = re.sub('[()]','', soup.find(text=target).find_parent().find_parent().find_all('td')[1].text)

        scale = ''
        if unit == '千円':
            scale ='000'
        elif unit == '百万円':
            scale = '000000'
        elif unit == '億円':
            scale = '00000000'
        else:
            pass
        return re.sub('[^0-9]','', soup.find(text=target).find_parent().find_parent().find_all('td')[6].text) + scale

    def scraping_client_information(self):
        print('クライアント情報更新開始')

        for i in range(self.PAGE_LIMIT):
            response = requests.get(self.SIGHT_URL + self.AUDIT_CODE_DICT[self.audit_code]['client_url'] + str(i+1))
            # pylint: disable=E1101
            if response.status_code != requests.codes.ok:
                print('担当企業一覧ページはこれ以上ありません。')
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
                try :

                    table = base.classes.gis_utils_app_client
                    model = table(
                        s_code = soup.find('h2').contents[0].strip().split(' ')[0],
                        name = soup.find('h2').contents[0].strip().split(' ')[1].replace('\u3000', ' '),
                        street_address = soup.find(id='address2').find('a').contents[0].strip()[9:],
                        longitude = None,
                        latitude = None,
                        employees = re.sub(r'[^0-9]','', soup.find(text='従業員数').find_parent().find_parent().find_all('dd')[0].text),
                        average_age = self.cast_decimal(re.sub(r'[^0-9\.]','', soup.find(text='平均年齢').find_parent().find_parent().find_all('dd')[1].text), "Decimal"),
                        service_years = self.cast_decimal(re.sub(r'[^0-9\.]','', soup.find(text='平均勤続年数').find_parent().find_parent().find_all('dd')[2].text), "Decimal"),
                        income = re.sub(r'[^0-9]','', soup.find(text='年間給与').find_parent().find_parent().find_all('dd')[3].text),
                        sales = self.adjust_scale(soup, '売上高'),
                        ordinary_income = self.adjust_scale(soup, '経常利益又は経常損失（△）'),
                        net_income = self.adjust_scale(soup, '当期純利益又は当期純損失（△）'),
                        audit_code = self.audit_code
                    )
                except Exception as e:
                    print('スクレイピングエラー count:%d' % self.count)
                    print(e)
                    continue

                models.append(model)
                self.print_model_client(model)
                self.count = self.count + 1
                time.sleep(3)

            self.session.add_all(models)

        print('クライアント情報更新完了')

    def cast_decimal(self, value, ctype):
        if not value:
            return None
        if (ctype == "Decimal"):
            return Decimal(value)
        else:
            return None

    def print_model_client(self, model):
        print(model.s_code, model.name, model.street_address, model.longitude, model.latitude, model.employees, model.average_age, model.service_years, model.income, model.sales, model.ordinary_income, model.net_income, model.audit_code)

    def request_geocoding(self):
        print('geocoding情報更新開始')

        table = base.classes.gis_utils_app_client
        models = self.session.query(table).filter(table.audit_code==self.audit_code).all()
        for model in models:
            response = requests.get(url=self.GEOCODING_API_URL, params={'q': model.street_address})
            data = etree.fromstring(response.text)
            print(response.text)
            if data.find('error') is not None:
                continue
            lng = data.find('coordinate').find('lng').text
            lat = data.find('coordinate').find('lat').text
            model.longitude = lng
            model.latitude = lat
            print('s_code: %s, longitude: %s, latitude: %s' % (model.s_code, lng, lat))
            time.sleep(10)
        print('geocoding情報更新完了')

    def __init__(self, base, session, audit_code):
        self.base = base
        self.session = session
        self.audit_code = audit_code


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('audit_code')

    args = parser.parse_args()

    database_url = 'sqlite:///db.sqlite3'
    if 'DATABASE_URL' in os.environ:
        database_url = os.environ.get('DATABASE_URL', None)

    base = automap_base()
    engine = create_engine(
        database_url,
        encoding = "utf-8",
        echo=True # Trueだと実行のたびにSQLが出力される
    )
    base.prepare(engine, reflect=True)

    # Sessionの作成
    session = scoped_session(
        # ORM実行時の設定。自動コミットするか、自動反映するなど。
        sessionmaker(
            autocommit = False,
            autoflush = False,
            bind = engine
        )
    )

    exec = ScrapingAuditClientExecutor(base, session, args.audit_code)
    exec.pre_scraping()
    exec.scraping_client_information()
    session.commit()
    exec.request_geocoding()
    exec.post_scraping()
    # pylint: disable=E1101
    session.commit()
    session.close()


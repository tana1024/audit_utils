import requests
import re
import sqlite3
import sys
from bs4 import BeautifulSoup
from django.db import models
from contextlib import closing


class ScrapingAuditClientExecutor:

    def pre_scraping(self):
        with closing(sqlite3.connect('/workspace/gis_utils/gis_utils_project/db.sqlite3')) as conn:
            # pylint: disable=E1101
            c = conn.cursor()
            c.execute('delete from gis_utils_app_client where 1=1')
            conn.commit()
            conn.close()

    def scraping(self):

        for i in range(100):
            response = requests.get('https://xn--vckya7nx51ik9ay55a3l3a.com/analyses/auditor_clients/%EF%BC%A5%EF%BC%B9%E6%96%B0%E6%97%A5%E6%9C%AC%E6%9C%89%E9%99%90%E8%B2%AC%E4%BB%BB%E7%9B%A3%E6%9F%BB%E6%B3%95%E4%BA%BA?page=' + str(i+1))
            # pylint: disable=E1101
            if response.status_code != requests.codes.ok:
                print('担当企業一覧ページがありません。')
                return
            soup = BeautifulSoup(response.content, 'html.parser')
            a_list = soup.find_all('a', href=re.compile('.*/companies/.*'))
            h_list = list(map(lambda x: x['href'], a_list))

            models = []
            for h in h_list:
                response = requests.get('https://xn--vckya7nx51ik9ay55a3l3a.com/' + h)
                if response.status_code != requests.codes.ok:
                    print('担当企業詳細ページがありません。')
                    continue
                soup = BeautifulSoup(response.content, "html.parser")
                model = (
                    soup.find('h2').contents[0].strip().split(' ')[0],
                    soup.find('h2').contents[0].strip().split(' ')[1].replace('\u3000', ' '),
                    soup.find(id='address2').find('a').contents[0].strip()[9:] if len(soup.find(id='address2').find('a').contents) != 0 else 'N/A',
                    'sn'
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

    def init(self):
        pass


if __name__ == '__main__':
    exec = ScrapingAuditClientExecutor()
    exec.pre_scraping()
    exec.scraping()

import requests
import re
import sqlite3
from bs4 import BeautifulSoup
from django.db import models
from contextlib import closing


class ScrapingAuditClientExecutor:

    model = None

    def scraping(self):
        response = requests.get('https://xn--vckya7nx51ik9ay55a3l3a.com/analyses/auditor_clients/%EF%BC%A5%EF%BC%B9%E6%96%B0%E6%97%A5%E6%9C%AC%E6%9C%89%E9%99%90%E8%B2%AC%E4%BB%BB%E7%9B%A3%E6%9F%BB%E6%B3%95%E4%BA%BA?page=1')
        soup = BeautifulSoup(response.content, "html.parser")
        a_list = soup.find_all('a', href=re.compile('.*/companies/.*'))
        h_list = list(map(lambda x: x['href'], a_list))
        print(h_list)

        response = requests.get('https://xn--vckya7nx51ik9ay55a3l3a.com/' + h_list[0])
        soup = BeautifulSoup(response.content, "html.parser")
        self.model = {
            's_code': soup.find('h2').contents[0].strip().split(' ')[0],
            'name': soup.find('h2').contents[0].strip().split(' ')[1],
            'street_address': soup.find(id='address2').find('a').contents[0].strip()[9:]
        }

    def insert(self):
        with closing(sqlite3.connect('/workspace/gis_utils/gis_utils_project/db.sqlite3')) as conn:
            # pylint: disable=E1101
            c = conn.cursor()
            for row in c.execute('select * from gis_utils_app_spot'):
                print(row)
            conn.commit()
            conn.close()

    def init(self):
        pass


if __name__ == '__main__':
    exec = ScrapingAuditClientExecutor()
    # exec.scraping()
    exec.insert()

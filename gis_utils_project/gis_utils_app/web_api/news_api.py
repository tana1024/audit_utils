import os
import yaml
import smtplib
from datetime import datetime as dt
from pytz import timezone
from dateutil.relativedelta import relativedelta as rdelta
from newsapi import NewsApiClient
from googletrans import Translator
from email.mime.text import MIMEText

from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker, scoped_session
from sqlalchemy.ext.automap import automap_base

class DelegateNewsApi:

    API_ID = '1'
    STATUS_PROGRESS = '1'
    STATUS_COMPLETE = '2'

    message = "ニュースの更新が完了しました。\n" + \
              "更新件数: %d"
    count = 0
    limit = 10
    api_key = mail_server = from_mail_address = from_mail_password = to_mail_address = ''
    newsapi = translator = base = session = None

    def pre_news(self):
        table = self.base.classes.gis_utils_app_newsupdatestatus
        self.session.query(table).filter(table.api_id==self.API_ID).delete()
        self.session.add(table(api_id=self.API_ID, status=self.STATUS_PROGRESS, update_count=None, update_datetime=dt.now(timezone('UTC'))))
        table = self.base.classes.gis_utils_app_news
        self.session.query(table).delete()

    def post_news(self):
        print('ニュース更新の通知処理開始')

        table = self.base.classes.gis_utils_app_newsupdatestatus
        model = self.session.query(table).filter(table.api_id==self.API_ID).first()
        model.status = self.STATUS_COMPLETE
        model.update_count = self.count
        model.update_datetime = dt.now(timezone('UTC'))

        # MIMEの作成
#        subject = "ニュース更新の完了通知"
#        self.message = self.message % (self.count)
#        msg = MIMEText(self.message, 'plain')
#        msg["Subject"] = subject
#        msg["To"] = self.to_mail_address
#        msg["From"] = self.from_mail_address

#        server = smtplib.SMTP(self.mail_server, 465)
#        server.starttls()
#        server.login(self.from_mail_address, self.from_mail_password)
#        server.send_message(msg)
#        server.quit()

        print('ニュース更新の通知処理終了')

    def get_news(self):
        print('ニュース取得開始')
        now = dt.now()
        table = self.base.classes.gis_utils_app_newsadmin
        news_admins = self.session.query(table)
        
        for news_admin in news_admins:
            print(news_admin.serch_keyword)
            news =  self.newsapi.get_everything(q=news_admin.serch_keyword.replace(' ', ' AND '), from_param=(now - rdelta(months=1)).strftime('%Y-%m-%d'), to=now.strftime('%Y-%m-%d'))
            print(news)

            if (news['totalResults'] == 0):
                print('取得したニュースはありません。')
                continue

            self.limit = int(news['totalResults']) if self.limit > int(news['totalResults']) else self.limit   
            models = []
            for i in range(self.limit):
                print('count : %d' % i)
                article = news['articles'][i]
                table = self.base.classes.gis_utils_app_news
                model = table(
                    source_id = article['source']['id'] or "",
                    source_name = article['source']['name'] or "",
                    author = article['author'] or "",
                    title = article['title'] or "",
                    # google翻訳の上限に注意
                    title_jp = self.translator.translate(article['title'], dest='ja').text or "",
#                    title_jp = 'google 翻訳機能停止中',
                    description = article['description'] or "",
                    # google翻訳の上限に注意
                    description_jp = self.translator.translate(article['description'], dest='ja').text or "",
#                    description_jp = 'google 翻訳機能停止中',
                    url = article['url'] or "",
                    url_to_image = article['urlToImage'] or "",
                    published_at = dt.fromisoformat(article['publishedAt'].replace('Z', '+00:00')) if article['publishedAt'] != None else article['publishedAt'],
                    content = article['content'] or "",
                    topic_id = news_admin.topic_id
                )
                models.append(model)
                self.count = self.count + 1

            self.session.add_all(models)
            print('ニュース取得終了')

    def commit(self):
        self.session.commit()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, trace):
        print('__exit__:', ex_type, ex_value, trace)
        self.session.close()

    def __init__(self):
        # クライアントを初期化
        django_root = os.environ.get('DJANGO_ROOT', None)
        with open(django_root + '/parameter.yaml') as file:
            yml = yaml.load(file, Loader=yaml.SafeLoader)
            api_key = yml['news_api']['api_key']
            self.mail_server = yml['contact']['server']
            self.from_mail_address = yml['contact']['from']['mail_address']
            self.from_mail_password = yml['contact']['from']['mail_password']
            self.to_mail_address = yml['contact']['to']['mail_address']


        self.newsapi = NewsApiClient(api_key=api_key)

        self.translator = Translator()

        database_url = 'sqlite:///%s/db.sqlite3' % (django_root)
        if 'DATABASE_URL' in os.environ:
            database_url = os.environ.get('DATABASE_URL', None)

        self.base = automap_base()
        engine = create_engine(
            database_url,
            encoding = "utf-8",
            echo=True # Trueだと実行のたびにSQLが出力される
        )
        self.base.prepare(engine, reflect=True)

        # Sessionの作成
        self.session = scoped_session(
            # ORM実行時の設定。自動コミットするか、自動反映するなど。
            sessionmaker(
                autocommit = False,
                autoflush = False,
                bind = engine
            )
        )
        print('__init__')

if __name__ == '__main__':

    with DelegateNewsApi() as delegator:
        print('start')
        delegator.pre_news()
        delegator.commit()
        delegator.get_news()
        delegator.commit()
        delegator.post_news()
        delegator.commit()
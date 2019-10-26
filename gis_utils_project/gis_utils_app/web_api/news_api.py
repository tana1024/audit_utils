import os
import yaml
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rdelta
from newsapi import NewsApiClient
from googletrans import Translator

from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker, scoped_session
from sqlalchemy.ext.automap import automap_base

class DelegateNewsApi:

    limit = 10
    api_key = ''
    newsapi = translator = base = session = None

    def pre_news(self):
        table = self.base.classes.gis_utils_app_news
        self.session.query(table).delete()

    def get_news(self):
        print('ニュース取得開始')
        now = dt.now()
        news =  self.newsapi.get_everything(q='audit', from_param=(now - rdelta(months=1)).strftime('%Y-%m-%d'), to=now.strftime('%Y-%m-%d'))
        print(news)

        if (news['totalResults'] == 0):
            print('取得したニュースはありません。')

        self.limit = int(news['totalResults']) if self.limit > int(news['totalResults']) else self.limit
        models = []
        for i in range(self.limit):
            article = news['articles'][i]
            table = self.base.classes.gis_utils_app_news
            model = table(
                source_id = article['source']['id'] or "",
                source_name = article['source']['name'] or "",
                author = article['author'] or "",
                title = article['title'] or "",
                title_jp = self.translator.translate(article['title'], dest='ja').text or "",
                description = article['description'] or "",
                description_jp = self.translator.translate(article['description'], dest='ja').text or "",
                url = article['url'] or "",
                url_to_image = article['urlToImage'] or "",
                published_at = dt.fromisoformat(article['publishedAt'].replace('Z', '+00:00')) if article['publishedAt'] != None else article['publishedAt'],
                content = article['content'] or ""
            )
            models.append(model)

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
        self.newsapi = NewsApiClient(api_key=api_key)

        self.translator = Translator()

        database_url = 'sqlite:///db.sqlite3'
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
        delegator.get_news()
        delegator.commit()
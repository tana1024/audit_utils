from django.test import TestCase
from django.urls import reverse
from ....models import News
from ...factory.NewsFactory import NewsFactory, NewsAllFuzzyFactory
import datetime
import pytz

# Create your tests here.
class InitInformationViewTest(TestCase):
    URL_ROOT = '/api'

    def setUp(self):
        print('setUp start')

    def test_init_single(self):
        print('test_init_single start')
        factory = NewsFactory
        factory.create_batch(size=1)

        url = reverse('publish_information_view', urlconf='gis_utils_app.urls')
        print(url)
        response = self.client.get(self.URL_ROOT + url, {'selected': 'PwC'})
        print(response.data)
        self.assertEquals(response.status_code, 200)        
        self.assertEquals(response.data[0]['source_name'], 'hogehoge_news')
        self.assertEquals(response.data[0]['title'], 'comming alien')
        self.assertEquals(response.data[0]['title_jp'], 'エイリアンが来た')
        self.assertEquals(response.data[0]['description'], 'comming alien')
        self.assertEquals(response.data[0]['description_jp'], 'エイリアンが来た')
        self.assertEquals(response.data[0]['url'], 'https://hogehoge.hoge.hoge')
        self.assertEquals(response.data[0]['published_at'], '2019-01-16T01:17:30+09:00')

        News.objects.all().delete()

    def test_init_multi(self):
        print('test_init_multi start')
        factory = NewsAllFuzzyFactory
        factory.create_batch(size=10)

        url = reverse('publish_information_view', urlconf='gis_utils_app.urls')
        print(url)
        response = self.client.get(self.URL_ROOT + url, {'selected': 'PwC'})
        print(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), 10)

        News.objects.all().delete()

    def tearDown(self):
        print('tearDown start')

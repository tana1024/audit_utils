from django.test import TestCase
from django.urls import reverse
from ....models import News
from ...factory.NewsFactory import NewsFactory

# Create your tests here.
class InitInformationViewTest(TestCase):
    URL_ROOT = '/api'

    def setUp(self):
        print('setUp start')
        factory = NewsFactory
        factory.create_batch(size=10)

    def test_init(self):
        print('test_init start')
        url = reverse('init_information_view', urlconf='gis_utils_app.urls')
        print(url)
        response = self.client.get(self.URL_ROOT + url)
        print(response.data)
        self.assertEquals(response.status_code, 200)

    def tearDown(self):
        print('tearDown start')
        News.objects.all().delete()
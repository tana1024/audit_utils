import datetime
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyText, FuzzyDateTime
from ...models import News

class NewsFactory(DjangoModelFactory):
    
    class Meta : 
        model = News

    source_id = FuzzyText(length=50)
    source_name = FuzzyText(length=150)
    author = FuzzyText(length=50)
    title = FuzzyText(length=250)
    title_jp = FuzzyText(length=250)
    description = FuzzyText(length=500)
    description_jp = FuzzyText(length=500)
    url = FuzzyText(length=150)
    url_to_image = FuzzyText(length=250)
    published_at = FuzzyDateTime(datetime.datetime(2010, 1, 1, tzinfo=datetime.timezone.utc))
    content = FuzzyText(length=500)
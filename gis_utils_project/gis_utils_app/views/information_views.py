from rest_framework.generics import ListAPIView
from ..models import News
from ..serializers import NewsSerializer

# pylint: disable=E1101
class InitInformationView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
from rest_framework.generics import ListAPIView
from ..models import News
from ..serializers import NewsSerializer

# pylint: disable=E1101
class PublishInformationView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.all()
        queryset = queryset.filter(topic_id=self.request.query_params['selected'])
        return queryset
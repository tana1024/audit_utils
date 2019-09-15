from distutils.util import strtobool

from rest_framework.generics import ListAPIView

from ..models import Client
from ..serializers import ClientSerializer

# pylint: disable=E1101
class GetClientGioInfoView(ListAPIView):

    serializer_class = ClientSerializer

    def get_queryset(self):
        if not bool(strtobool(self.request.query_params['check_sn'])) and \
           not bool(strtobool(self.request.query_params['check_az'])) and \
           not bool(strtobool(self.request.query_params['check_dt'])) and \
           not bool(strtobool(self.request.query_params['check_ar'])):
            return Client.objects.none()

        queryset = Client.objects.all()

        queryset = queryset.exclude(longitude=None, latitude=None)
        filter_element = []
        if bool(strtobool(self.request.query_params['check_sn'])):
            filter_element.append('sn')
        if bool(strtobool(self.request.query_params['check_az'])):
            filter_element.append('az')
        if bool(strtobool(self.request.query_params['check_dt'])):
            filter_element.append('dt')
        if bool(strtobool(self.request.query_params['check_ar'])):
            filter_element.append('ar')
        if filter_element:
            queryset = queryset.filter(audit_code__in=filter_element)

        return queryset
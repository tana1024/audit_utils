from abc import ABCMeta, abstractmethod
from distutils.util import strtobool

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from ..models import Client
from ..serializers import ClientBarChartSerializer, ClientAverageAgeChartSerializer, ClientServiceYearsChartSerializer, ClientOrdinaryIncomeChartSerializer, ClientNetIncomeChartSerializer

# pylint: disable=E1101
class AbstractScatterChartDataView(ListAPIView, metaclass=ABCMeta):

    @abstractmethod
    def queryset_exclude_of_child(self, queryset):
        raise NotImplementedError()

    def get_queryset(self):
        if not bool(strtobool(self.request.query_params['check_sn'])) and \
           not bool(strtobool(self.request.query_params['check_az'])) and \
           not bool(strtobool(self.request.query_params['check_dt'])) and \
           not bool(strtobool(self.request.query_params['check_ar'])):
            return Client.objects.none()

        queryset = Client.objects.all()
        queryset = self.queryset_exclude_of_child(queryset)
        queryset = queryset.exclude(income=0)
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

class GetClientAverageAgeChartDataView(AbstractScatterChartDataView):
    serializer_class = ClientAverageAgeChartSerializer

    def queryset_exclude_of_child(self, queryset):
        return queryset.exclude(average_age=0).exclude(income=0)

class GetClientServiceYearsChartDataView(AbstractScatterChartDataView):
    serializer_class = ClientServiceYearsChartSerializer

    def queryset_exclude_of_child(self, queryset):
        return queryset.exclude(service_years=0).exclude(income=0)

class GetClientOrdinaryIncomeChartDataView(AbstractScatterChartDataView):
    serializer_class = ClientOrdinaryIncomeChartSerializer

    def queryset_exclude_of_child(self, queryset):
        return queryset.exclude(sales=0).exclude(ordinary_income=0)

class GetClientNetIncomeChartDataView(AbstractScatterChartDataView):
    serializer_class = ClientNetIncomeChartSerializer

    def queryset_exclude_of_child(self, queryset):
        return queryset.exclude(sales=0).exclude(net_income=0)
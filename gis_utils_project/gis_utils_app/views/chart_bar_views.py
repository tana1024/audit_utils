from abc import ABCMeta, abstractmethod
from distutils.util import strtobool

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from ..models import Client
from ..serializers import ClientBarChartSerializer, ClientAverageAgeChartSerializer, ClientServiceYearsChartSerializer

# pylint: disable=E1101
class AbstractBarChartDataView(ListAPIView, metaclass=ABCMeta):

    serializer_class = ClientBarChartSerializer

    @abstractmethod
    def aggregate(self, audit_code):
        raise NotImplementedError()

    @abstractmethod
    def get_queryset(self, audit_code, under, over):
        raise NotImplementedError()


    def list(self, request):
        if not bool(strtobool(self.request.query_params['check_sn'])) and \
           not bool(strtobool(self.request.query_params['check_az'])) and \
           not bool(strtobool(self.request.query_params['check_dt'])) and \
           not bool(strtobool(self.request.query_params['check_ar'])):
            return Response([]) #  return empty

        list_aggregate = []
        if bool(strtobool(self.request.query_params['check_sn'])):
            list_aggregate.append(self.aggregate('sn'))
        if bool(strtobool(self.request.query_params['check_az'])):
            list_aggregate.append(self.aggregate('az'))
        if bool(strtobool(self.request.query_params['check_dt'])):
            list_aggregate.append(self.aggregate('dt'))
        if bool(strtobool(self.request.query_params['check_ar'])):
            list_aggregate.append(self.aggregate('ar'))

        serializer = self.get_serializer(data=list_aggregate, many=True)
        serializer.is_valid()
        return Response(serializer.validated_data)


class GetClientEmployeesChartDataView(AbstractBarChartDataView):

    def get_queryset(self, audit_code, under, over=None):
        queryset = Client.objects.all()
        queryset = queryset.filter(audit_code=audit_code)
        queryset = queryset.filter(employees__lt=over) if over else queryset
        queryset = queryset.filter(employees__gte=under)
        return len(queryset)

    def aggregate(self, audit_code):
        return {
            'audit_code': audit_code,
            'count_section1': self.get_queryset(audit_code, 0, 100),
            'count_section2': self.get_queryset(audit_code, 100, 300),
            'count_section3': self.get_queryset(audit_code, 300, 1000),
            'count_section4': self.get_queryset(audit_code, 1000, 3000),
            'count_section5': self.get_queryset(audit_code, 3000, 10000),
            'count_section6': self.get_queryset(audit_code, 10000)
        }

class GetClientIncomeChartDataView(AbstractBarChartDataView):

    def get_queryset(self, audit_code, under, over=None):
        queryset = Client.objects.all()
        queryset = queryset.filter(audit_code=audit_code)
        queryset = queryset.filter(income__lt=over) if over else queryset
        queryset = queryset.filter(income__gte=under)
        return len(queryset)

    def aggregate(self, audit_code):
        return {
            'audit_code': audit_code,
            'count_section1': self.get_queryset(audit_code, 0, 400),
            'count_section2': self.get_queryset(audit_code, 400, 600),
            'count_section3': self.get_queryset(audit_code, 600, 8000),
            'count_section4': self.get_queryset(audit_code, 800, 1000),
            'count_section5': self.get_queryset(audit_code, 1000, 1300),
            'count_section6': self.get_queryset(audit_code, 1300)
        }

class GetClientSalesChartDataView(AbstractBarChartDataView):

    def get_queryset(self, audit_code, under, over=None):
        queryset = Client.objects.all()
        queryset = queryset.filter(audit_code=audit_code)
        queryset = queryset.filter(sales__lt=over) if over else queryset
        queryset = queryset.filter(sales__gte=under)
        return len(queryset)

    def aggregate(self, audit_code):
        return {
            'audit_code': audit_code,
            'count_section1': self.get_queryset(audit_code, 0, 10000000000),
            'count_section2': self.get_queryset(audit_code, 10000000000, 30000000000),
            'count_section3': self.get_queryset(audit_code, 30000000000, 100000000000),
            'count_section4': self.get_queryset(audit_code, 100000000000, 300000000000),
            'count_section5': self.get_queryset(audit_code, 300000000000, 1000000000000),
            'count_section6': self.get_queryset(audit_code, 1000000000000)
        }

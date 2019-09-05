import subprocess
from distutils.util import strtobool

from django.http import HttpResponse

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Client, ClientUpdateStatus, Spot
from .renderers import SpotJSONRenderer
from .serializers import ClientSerializer, ClientUpdateStatusSerializer, ClientEmployeeChartSerializer, SpotListSerializer, SpotSerializer
from .scraping.scraping_audit_client import ScrapingAuditClientExecutor


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class InitScraping(generics.ListAPIView):
    # pylint: disable=E1101
    queryset = ClientUpdateStatus.objects.all()
    serializer_class = ClientUpdateStatusSerializer


class ExecScraping(APIView):

    def get(self, request):
        if 'audit_code' in request.query_params:
            cmd = "bash ./gis_utils_app/scraping/launch_scraping.sh " + request.query_params['audit_code']
            subprocess.Popen(cmd.split())
        return Response('accepted update')


class GetClientGioInfo(generics.ListAPIView):

    serializer_class = ClientSerializer

    def get_queryset(self):
        # pylint: disable=E1101
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


class GetClientEmployeeChartData(generics.ListAPIView):

    serializer_class = ClientEmployeeChartSerializer

    def get_queryset(self):
        # pylint: disable=E1101
        queryset = Client.objects.all()
        queryset = queryset.filter(audit_code='dt')
        queryset = queryset.filter(employees__lte=500)
        queryset = queryset.filter(employees__gte=100)
        return len(queryset)

    def list(self, request):
        count = self.get_queryset()
        serializer = self.get_serializer(data={'count': count})
        serializer.is_valid()
        return Response(serializer.validated_data)


# pylint: disable=E1101
class SpotListApiView(ListAPIView):
    model = Spot
    queryset = Spot.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (SpotJSONRenderer, )
    serializer_class = SpotListSerializer


class SpotRetrieveApiView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (SpotJSONRenderer, )
    serializer_class = SpotSerializer

    def retrieve(self, request, spot_id, *args, **kwargs):
        spot = Spot.objects.get(id=spot_id)
        serializer = self.serializer_class(spot)

        return Response(serializer.data, status=status.HTTP_200_OK)

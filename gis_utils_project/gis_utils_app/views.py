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
from .serializers import ClientSerializer, ClientUpdateStatusSerializer, SpotListSerializer, SpotSerializer
from .scraping.scraping_audit_client import ScrapingAuditClientExecutor


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class InitScraping(generics.ListAPIView):
    # pylint: disable=E1101
    queryset = ClientUpdateStatus.objects.all()
    serializer_class = ClientUpdateStatusSerializer


class ExecScraping(APIView):

    def get(self, request, *args, **kwargs):
        if 'audit_code' in request.query_params:
            cmd = "bash ./gis_utils_app/scraping/launch_scraping.sh " + request.query_params['audit_code']
            subprocess.Popen(cmd.split())
        return Response('accepted update')


class GetClientGioInfo(generics.ListAPIView):
    # pylint: disable=E1101
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.all()
        queryset = queryset.exclude(longitude=None, latitude=None)
        filter = []
        if bool(strtobool(self.request.query_params['check_sn'])):
            filter.append('sn')
        if bool(strtobool(self.request.query_params['check_az'])):
            filter.append('az')
        if bool(strtobool(self.request.query_params['check_dt'])):
            filter.append('dt')
        if bool(strtobool(self.request.query_params['check_ar'])):
            filter.append('ar')

        if len(filter) != 0:
            queryset = queryset.filter(audit_code__in=filter)

        return queryset


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

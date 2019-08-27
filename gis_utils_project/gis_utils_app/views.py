import subprocess
from .scraping.scraping_audit_client import ScrapingAuditClientExecutor
from django.http import HttpResponse

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import ClientUpdateStatus, Spot
from .renderers import SpotJSONRenderer
from .serializers import ClientUpdateStatusSerializer, SpotListSerializer, SpotSerializer


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

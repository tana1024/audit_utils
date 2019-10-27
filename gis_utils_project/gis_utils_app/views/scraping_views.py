import os
import subprocess

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import ClientUpdateStatus, NewsUpdateStatus
from ..serializers import ClientUpdateStatusSerializer, NewsUpdateStatusSerializer

# pylint: disable=E1101
class InitScrapingView(ListAPIView):
    queryset = ClientUpdateStatus.objects.all()
    serializer_class = ClientUpdateStatusSerializer

class InitWebApiView(ListAPIView):
    queryset = NewsUpdateStatus.objects.all()
    serializer_class = NewsUpdateStatusSerializer

class ExecScrapingView(APIView):

    def get(self, request):
        if 'audit_code' in request.query_params:
            django_root = os.environ.get('DJANGO_ROOT', None)
            cmd = "bash %s/bash/launch_scraping.sh %s" % (django_root, request.query_params['audit_code'])
            subprocess.Popen(cmd.split())
        return Response('accepted update')

class ExecWebApiView(APIView):

    def get(self, request):
        django_root = os.environ.get('DJANGO_ROOT', None)
        cmd = "bash %s/bash/launch_webapi.sh" % (django_root)
        subprocess.Popen(cmd.split())
        return Response('accepted update')
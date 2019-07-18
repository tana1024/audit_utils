from django.urls import path
from django.conf.urls import url

from . import views
from .views import SpotListApiView, SpotRetrieveApiView

app_name = 'gis_utils_app'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^spots/$', SpotListApiView.as_view()),
    url(r'^spots/(?P<spot_id>\w+)/?$', SpotRetrieveApiView.as_view()),
]
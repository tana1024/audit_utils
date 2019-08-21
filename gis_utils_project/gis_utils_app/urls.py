from django.urls import path
from django.conf.urls import url

from . import views
from .views import InitScraping, ExecScraping, SpotListApiView, SpotRetrieveApiView

app_name = 'gis_utils_app'
urlpatterns = [
    path('hello', views.index, name='index'),
    path('init_scraping', InitScraping.as_view()),
    path('exec_scraping', ExecScraping.as_view()),
    url(r'^spots/$', SpotListApiView.as_view()),
    url(r'^spots/(?P<spot_id>\w+)/?$', SpotRetrieveApiView.as_view()),
]
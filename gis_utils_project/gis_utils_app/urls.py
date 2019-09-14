from django.urls import path
from django.conf.urls import url

from . import views
from .views import InitScraping, ExecScraping, GetClientGioInfo, GetClientEmployeesChartData, GetClientAverageAgeChartData, SpotListApiView, SpotRetrieveApiView

app_name = 'gis_utils_app'
urlpatterns = [
    path('hello', views.index, name='index'),
    path('scraping/init_scraping', InitScraping.as_view()),
    path('scraping/exec_scraping', ExecScraping.as_view()),
    path('map/get_client_gio_info', GetClientGioInfo.as_view()),
    path('chart/get_client_employees_chart_data', GetClientEmployeesChartData.as_view()),
    path('chart/get_client_average_age_chart_data', GetClientAverageAgeChartData.as_view()),
    url(r'^spots/$', SpotListApiView.as_view()),
    url(r'^spots/(?P<spot_id>\w+)/?$', SpotRetrieveApiView.as_view()),
]
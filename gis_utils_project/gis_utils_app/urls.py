from django.urls import path
from django.conf.urls import url

from .views import views
from .views.information_views import PublishInformationView
from .views.scraping_views import InitScrapingView, ExecScrapingView, InitWebApiView, ExecWebApiView
from .views.mapping_views import GetClientGioInfoView
from .views.chart_bar_views import GetClientEmployeesChartDataView, GetClientIncomeChartDataView, GetClientSalesChartDataView
from .views.chart_scatter_views import GetClientAverageAgeChartDataView, GetClientServiceYearsChartDataView, GetClientOrdinaryIncomeChartDataView, GetClientNetIncomeChartDataView
from .views.views import SpotListApiView, SpotRetrieveApiView

app_name = 'gis_utils_app'
urlpatterns = [
    path('hello', views.index, name='index'),
    path('information/publish_information', PublishInformationView.as_view(), name="publish_information_view"),
    path('scraping/init_scraping', InitScrapingView.as_view(), name="initScrapingView"),
    path('scraping/init_webapi', InitWebApiView.as_view(), name="initWebApiView"),
    path('scraping/exec_scraping', ExecScrapingView.as_view(), name="execScrapingView"),
    path('scraping/exec_webapi', ExecWebApiView.as_view(), name="execWebApiView"),
    path('map/get_client_gio_info', GetClientGioInfoView.as_view(), name="getClientGioInfoView"),
    path('chart/get_client_employees_chart_data', GetClientEmployeesChartDataView.as_view(), name="getClientEmployeesChartDataView"),
    path('chart/get_client_average_age_chart_data', GetClientAverageAgeChartDataView.as_view(), name="getClientAverageAgeChartDataView"),
    path('chart/get_client_service_years_chart_data', GetClientServiceYearsChartDataView.as_view(), name="getClientServiceYearsChartDataView"),
    path('chart/get_client_income_chart_data', GetClientIncomeChartDataView.as_view(), name="getClientIncomeChartDataView"),
    path('chart/get_client_sales_chart_data', GetClientSalesChartDataView.as_view(), name="getClientSalesChartDataView"),
    path('chart/get_client_ordinary_income_chart_data', GetClientOrdinaryIncomeChartDataView.as_view(), name="getClientOrdinaryIncomeChartDataView"),
    path('chart/get_client_net_income_chart_data', GetClientNetIncomeChartDataView.as_view(), name="getClientNetIncomeChartDataView")
    # url(r'^spots/$', SpotListApiView.as_view()),
    # url(r'^spots/(?P<spot_id>\w+)/?$', SpotRetrieveApiView.as_view()),
]
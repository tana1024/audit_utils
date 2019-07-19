"""gis_utils_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include as cinclude, url
from rest_framework import routers
from gis_utils_app import urls

from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gis_utils_app/', include('gis_utils_app.urls')),
    url('api/', cinclude(router.urls)),
    url('api/', cinclude(urls, namespace='gis_utils_app')),
    url('', TemplateView.as_view(template_name='gis_utils_frontend/index.html'), name='Home'),
]

urlpatterns += staticfiles_urlpatterns()
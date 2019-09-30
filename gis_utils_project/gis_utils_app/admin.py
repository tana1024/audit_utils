from django.contrib import admin

from .models import ClientUpdateStatus, Client

# Register your models here.
admin.site.register(ClientUpdateStatus)
admin.site.register(Client)
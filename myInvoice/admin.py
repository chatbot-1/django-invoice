from django.contrib import admin
from .models import Client, Service, Add_service

# Register your models here.
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Add_service)


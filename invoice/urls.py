"""
URL configuration for invoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myInvoice.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', log_in, name='login'),
    path('signup/', sign_up, name='signup'),
    path('logout/', log_out, name='logout'),
    path('add_service/', provider, name='addService'),
    path('add_client/', client, name='client'),
    path('service/', service, name='service'),
    path('delete_service/<id>/', delete_provider, name='delService'),
    path('update_service/<id>/', update_provider, name='upService'),
    path('view-client/', viewClient, name='viewClient'),
    path('delete_client/<id>/', delete_client, name='delClient'),
    path('update_client/<id>/', update_client, name='upClient'),
    path('show_client/<id>/', show_client, name='showClient'),
    path('update_service/<id>/', update_service, name='update_service'),
    path('delete_service/<id>/', delete_service, name='delete_service'),
]

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
    path('add_service/', add_service, name='addService'),
    path('add_client/', client, name='client'),
    path('service/', service, name='service'),
    # path('ajax/load-client/', load_client, name='loadClient'),
]

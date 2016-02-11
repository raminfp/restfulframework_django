"""django_restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from rest_service.views import api_select, api_del, api_up


urlpatterns = [
    url(r'selectall^$', api_select ),
    url(r'^$', api_select ),
    url(r'insert^$', api_select ),
    url(r'^update/(?P<pk>[0-9]+)$', api_up ),
    url(r'^delete/(?P<pk>[0-9]+)$', api_del ),
]

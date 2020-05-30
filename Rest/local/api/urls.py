"""Rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from .views import (StatusApiView,
                    # StatusCreateApiView,
                    StatusApiDetailView,
                    # StatusUpdateApiView,
                    # StatusDeleteApiView
                    )





urlpatterns = [
    url(r'^$', StatusApiView.as_view()),  # /api/status/->List,create
    url(r'^(?P<id>\d+)/$', StatusApiDetailView.as_view())
    #url(r'^(?P<id>\d+)/$', StatusDetailApiView.as_view()),  # /api/status/any-id/->Details,update,delete
    # url(r'^create/$', StatusCreateApiView.as_view()),  # /api/status/create->create   //this is handled by StatusApiView
    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateApiView.as_view()),  # /api/status/any-id/update->update //this is handled by StatusDetailApiView
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteApiView.as_view()),  # /api/status/any-id/delete->delete //this is handled by StatusDetailApiView

]

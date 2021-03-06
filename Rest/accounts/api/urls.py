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

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import AuthAPIView,RegisterAPIView

urlpatterns = [
    url('', csrf_exempt(AuthAPIView.as_view())),
    url(r'^register/$', csrf_exempt(RegisterAPIView.as_view())),
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^refresh/$', refresh_jwt_token),
]

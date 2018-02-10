from django.conf.urls import url, include
from . import views

app_name = 'blogapp'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg/$', views.register),
]
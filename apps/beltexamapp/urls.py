from django.conf.urls import url, include
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'main$', views.index),
    url(r'register$', views.register),
    url(r'login$',views.login),
    url(r'travels$', views.travels),
    url(r'travels/add$', views.addplan),
    url(r'add$',views.add),
    url(r'travels/destination/(?P<variable>\d+)$', views.destination),
    url(r'join/(?P<variable>\d+)$', views.join)


]

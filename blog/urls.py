"""from django.conf.urls import re_path
from django.contrib import admin
from blog import views

urlpatterns = [
    re_path(r'^blog/', views.blog, name='blog'),
]
from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^blog/', views.blog, name='blog'),
]"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('', views.index, name='index'),
]
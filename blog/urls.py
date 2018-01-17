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
from django.urls import path, re_path
from blog.views import Index, Profile
# from . import views
from blog import views

urlpatterns = [
    # path('', views.Index, name='index'),
    # path('', Index.as_view(), name='index'),
    # path('', views.index, name='index'),
    #     path('', views.blog, name='blog'),
    # path('', Profile.as_view()),
    # re_path(r'^user/(\w+)/$', views.Profile, name='profile'),
    re_path(r'^user/', Profile.as_view(), name='profile')
]

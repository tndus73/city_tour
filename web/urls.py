from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
 #path('', views.homepage, name='homepage'),
 path('home/', views.home),
 path('header/', views.header),
 path('introduction/', views.introduction),
]
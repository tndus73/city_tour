from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
 #path('', views.homepage, name='homepage'),
 path('home/', views.home),
 path('homeCity/', views.homecity),
 path('header/', views.header),
 path('introduction/', views.introduction),
 path('manager/', views.manager),
 path('selectCity/', views.selectCity),
 path('whole_country/', views.whole_country),
]
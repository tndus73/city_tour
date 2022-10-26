from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
 #path('', views.homepage, name='homepage'),
 path('home/', views.home, name='home'),
 path('homeCity/', views.homecity, name='homeCity'),
 path('header/', views.header, name='header'),
 path('introduction/', views.introduction, name='introduction'),
 path('manager/', views.manager, name='manager'),
 path('selectCity/', views.selectCity, name='selectCity'),
 path('whole_country/', views.whole_country, name='whole_country'),

]
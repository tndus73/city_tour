from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
 #path('', views.homepage, name='homepage'),
 path('home/', views.home),
]
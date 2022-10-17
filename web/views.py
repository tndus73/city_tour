# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import time
from datetime import datetime
from .models import Citytourdata


def homepage(request) :
 return HttpResponse("<h1>홈페이지 만들어봅시다!!</h1>")

def home(request) :
 city1 = Citytourdata.objects.values('city1').distinct()
 city1_1=[]
 for i in range(0,len(city1),1):
  a = city1[i]
  city1_1.append(a.get('city1'))

 city2 = Citytourdata.objects.values('city2').distinct()
 city2_1=[]
 for i in range(0,len(city2),1):
  b = city2[i]
  city2_1.append(b.get('city2'))

 context = {
  'city1': city1_1,
  'city2': city2_1,
 }

 return render(request,"home.html", context)


def header(request):
 return render(request, 'header.html')

def introduction(request):
 return render(request,"introduction.html")

def manager(request):
 return render(request,"manager.html")




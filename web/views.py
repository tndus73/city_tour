from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Citytourdata
from django.http import JsonResponse
import json


def homepage(request) :
 return HttpResponse("<h1>홈페이지 만들어봅시다!!</h1>")

def homecity(request) :
 #시도 데이터 출력
 city1_data = Citytourdata.objects.values('city1').distinct()
 city1_order = city1_data.order_by('city1')
 list_city1=[]
 for i in range(0,len(city1_order),1):
  a = city1_order[i]
  list_city1.append(a.get('city1'))
 print(list_city1)
## 시도 선택 데이터
 selected_city1 = request.GET['selectedCity1']

## 시군구 데이터 출력
 dict_city2={}
 for i in range(0,len(list_city1),1):
  city = Citytourdata.objects.filter(city1=list_city1[i]).values()
  city2 = []
  for j in range(0,len(city),1):
   a = city[j].get('city2')
   city2.append(a)
  city2 = list(set(city2))
  city2.sort()
  dict_city2[list_city1[i]] = city2
 list_city2 = dict_city2.get(selected_city1)
 print(list_city2)
 return JsonResponse({"city2": list_city2}, json_dumps_params={'ensure_ascii':False}) #한국어 들어갈 때 필수.

def header(request):
 return render(request, 'header.html')

def introduction(request):
 return render(request,"introduction.html")

def manager(request):
 return render(request,"manager.html")

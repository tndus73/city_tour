from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Citytourdata
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

def homepage(request) :
 return HttpResponse("<h1>홈페이지 만들어봅시다!!</h1>")

def home(request) :
 #시도 데이터 출력
 city1_data = Citytourdata.objects.values('city1').distinct()
 city1_order = city1_data.order_by('city1')
 list_city1=[]
 for i in range(0,len(city1_order),1):
  a = city1_order[i]
  list_city1.append(a.get('city1'))
 context = {
  'city1' : list_city1
 }
 return render(request, 'home.html',context)

def homecity(request) :
 #시도 데이터 출력
 city1_data = Citytourdata.objects.values('city1').distinct()
 city1_order = city1_data.order_by('city1')
 list_city1=[]
 for i in range(0,len(city1_order),1):
  a = city1_order[i]
  list_city1.append(a.get('city1'))
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

  for k in range(0,len(city2),1):
   if city2[k] == '없음':
    city2[k] = list_city1[i]

  dict_city2[list_city1[i]] = city2
 list_city2 = dict_city2.get(selected_city1)
 return JsonResponse({"city2": list_city2}, json_dumps_params={'ensure_ascii':False}) #한국어 들어갈 때 필수.

def header(request):
 return render(request, 'header.html')

def introduction(request):
 return render(request,"introduction.html")

def manager(request):
 return render(request,"manager.html")

def selectCity(request):
 selected_city1 = request.GET['selectedCity1']
 selected_city2 = request.GET['selectedCity2']
 selectC = {'city1' : selected_city1 ,'city2' : selected_city2}
 nocity = ['울산광역시', '세종특별자치시','부산광역시']
 if selected_city2 in nocity:
  selected_city2 = '없음'
 city_data = Citytourdata.objects.filter(city1=selected_city1).values()
 city_datas = city_data.filter(city2=selected_city2).values()
 ## 선택한 지역의 시티투어 데이터 가져오기.
 tour_name = city_datas.values('cos_name')
 tour_name = tour_name.order_by('cos_name')
 list_tour = []
 for i in range(0, len(tour_name), 1):
  name = tour_name[i]
  list_tour.append(name.get('cos_name'))
 print(list_tour)
 ## 선택한 지역의 시티투어 이름 가져오기
 cityTour = []
 for cos_name in list_tour:
  selected_city_data = {}
  tourdata = Citytourdata.objects.filter(cos_name=cos_name).values()
  cos_info = tourdata[0].get('cos_info')
  start_time = tourdata[0].get('start_time')
  close_time = tourdata[0].get('close_time')
  url = tourdata[0].get('url')

  number = tourdata[0].get('number')
  ## 각 지역의 시티투어 딕셔너리 정보를 끌어옴
  selected_city_data['cos_name'] = cos_name
  selected_city_data['cos_info'] = cos_info
  selected_city_data['start_time'] = start_time
  selected_city_data['close_time'] = close_time
  selected_city_data['url'] = url
  selected_city_data['number'] = number
  ## 끌어온 정보를 시티투어별로 정리하여 밑에 리스트에 담음.
  cityTour.append(selected_city_data)
  for tour in cityTour:
   if tour.get('url') == "":
    tour['url'] = "준비 중입니다."
   if "http" not in tour.get('url'):
    if "kr" in tour.get('url') or "com" in tour.get('url') or "modoo" in tour.get('url') or "danyang" in tour.get('url'):
     tour['url'] = "http://" + tour.get('url')
 context = {
  'cityTours' : cityTour,
  'selectC' : selectC
 }
## 투어별 데이터 가져오기.
 return render(request, "selectCity.html", context)

def whole_country(request):
 tourdatas = Citytourdata.objects.values()
 tourdatas = tourdatas.order_by('city1')
 for data in tourdatas:
  if data.get('city2') == '없음':
   data['city2'] = data.get('city1')
  if data.get('url') == "":
   data['url'] = "준비 중입니다."
  if "http" not in data.get('url'):
   if "kr" in data.get('url') or "com" in data.get('url') or "modoo" in data.get('url') or "danyang" in data.get('url'):
    data['url'] = "http://"+ data.get('url')
 # 투어 데이터 가져오기
 q = request.GET.get('q', '')  #
 print(q)
 # value 가져오기
 if q == '':
  page = request.GET.get('page', 1)
  citytour_list = tourdatas
  paginator = Paginator(citytour_list, 15)
  page_obj = paginator.get_page(page)
  #  페이지 생성
  context = {
  "page_obj" : page_obj,
  }
  return render(request, "whole_country.html",context)
 else:
  page = request.GET.get('page', 1)
  citytour_list = tourdatas
  find_citytour_list =[]
  count = 0
  for i in range(0,len(citytour_list),1):
   if q in citytour_list[i].get('city1') or q in citytour_list[i].get('city2') or q in citytour_list[i].get('cos_name'):
    count+=1
    print(count,citytour_list[i])
    find_citytour_list.append(citytour_list[i])
  paginator = Paginator(find_citytour_list, 15)
  find_page_obj = paginator.get_page(page)
  #  페이지 생성
  context = {
  "find_page_obj" : find_page_obj,
   'q' : q ,
  }
  return render(request, "whole_country.html", context)





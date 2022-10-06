from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request) :
 return HttpResponse("<h1>홈페이지 만들어봅시다!!</h1>")

def home(request) :
 return render(request, 'home.html')
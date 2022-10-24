from django.contrib import admin

# Register your models here.
from django.contrib import admin

#게시글 Model 불러오기
from .models import Notice1

#관리자가 게시글에 접근가능하게
admin.site.register(Notice1)

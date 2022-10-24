from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    contents = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

        # 게시글 제목 나오게하기
    def __str__(self):
        return self.name

class Comment(models.Model):
  post = models.ForeignKey(Notice, on_delete=models.CASCADE, null=True)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
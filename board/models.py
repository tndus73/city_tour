from django.db import models

# Create your models here.
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=50)
    contents = models.TextField()

    #게시글 제목 나오게하기
    def __str__(self):
        return self.name
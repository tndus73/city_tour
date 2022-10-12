from django.db import models

# Create your models here.
class citytourdata(models.Model):
    city1 = models.CharField(max_length=50)
    city2 = models.CharField(max_length=50)
    cos_name = models.CharField(max_length=50)
    cos_info = models.CharField(max_length=200, null=True)
    start_time = models.CharField(max_length=50, null=True)
    close_time = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=50, null=True)

from django.db import models

# Create your models here.
class Citytourdata(models.Model):
    id = models.IntegerField(primary_key=True)
    city1 = models.CharField(max_length=50)
    city2 = models.CharField(max_length=50)
    cos_name = models.CharField(max_length=50)
    cos_info = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.CharField(max_length=50, blank=True, null=True)
    close_time = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.city1 +","+self.city2 +","+self.cos_name+\
            ","+self.cos_info+","+self.start_time+","+self.close_time+","+self.url+","+self.number
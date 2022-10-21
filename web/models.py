# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Create your models here.


class Citytourdata(models.Model):
    city1       = models.CharField(max_length=50)
    city2       = models.CharField(max_length=50)
    cos_name    = models.CharField(max_length=50)
    cos_info    = models.CharField(max_length=200, blank=True, null=True)
    start_time  = models.CharField(max_length=50, blank=True, null=True)
    close_time  = models.CharField(max_length=50, blank=True, null=True)
    url         = models.CharField(max_length=200, blank=True, null=True)
    number      = models.CharField(max_length=50, blank=True, null=True)
    id          = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.number+","+self.city1+","+self.city2+","+self.cos_name+","+self.cos_info+","+self.start_time+","+self.close_time+","+self.url+","+self.number

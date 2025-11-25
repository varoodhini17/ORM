from django.db import models
from django.contrib import admin

class car(models.Model):
    car_id=models.IntegerField()
    car_brand=models.CharField(max_length=50)
    car_year=models.IntegerField()
    car_reg=models.IntegerField()
    car_colour=models.CharField(max_length=50)

class carAdmin(admin.ModelAdmin):
    list_display=['car_id','car_brand','car_year','car_reg','car_colour']

# Create your models here.

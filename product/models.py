from django.db import models

# Create your models here.

class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
    Address=models.CharField(max_length=20,default="")
    Contact=models.IntegerField(default="")
    Email=models.CharField(max_length=20,default="")

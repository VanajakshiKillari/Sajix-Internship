from django.db import models
from django.contrib.auth.models import UserManager


class cruddb(models.Model):
    firstname = models.CharField(max_length=20, unique=True)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    phonenumber=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    address=models.CharField(max_length=40)
    objects = UserManager()
    
# Create your models here.

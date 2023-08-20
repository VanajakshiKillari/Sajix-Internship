from django.db import models
from django.contrib.auth.models import UserManager
class cruddb(models.Model):
    firstname = models.CharField(max_length=20, unique=True)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    objects = UserManager()
class cruddata(models.Model):
    username=models.CharField(max_length=20, unique=True)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    phonenumber=models.IntegerField()
    objects = UserManager()

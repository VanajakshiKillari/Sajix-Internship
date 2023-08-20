from django.db import models
from django.contrib.auth.models import UserManager
class cruddb(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    phonenumber=models.IntegerField()
    Email=models.CharField(max_length=30)
    dept=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    objects = UserManager()

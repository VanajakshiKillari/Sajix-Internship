from django.db import models


class modules(models.Model):
    module_name = models.CharField(max_length=50, null=True, default='DEFAULT VALUE')
    module_duration = models.IntegerField()
    class_room = models.IntegerField()
    objects = models.Manager


class student(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(modules)
    objects = models.Manager
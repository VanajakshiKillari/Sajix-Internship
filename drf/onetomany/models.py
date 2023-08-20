from django.db import models


class Library(models.Model):
    LibraryName = models.CharField(max_length=70)
    objects = models.manager


class Book(models.Model):
    Library = models.ForeignKey(Library, on_delete=models.CASCADE)
    BookName = models.CharField(max_length=70)
    AuthorName = models.CharField(max_length=70)
    objects = models.manager  

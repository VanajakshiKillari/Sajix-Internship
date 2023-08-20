from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from rest_framework.response import Response
from .serializers import Library1Serializer, Book1Serializer
from .models import *


# Create your views here.
class Library1View(generics.GenericAPIView):
    serializer_class = Library1Serializer

    def post(self, request, *args, **kwargs):
        a = Library1Serializer(data=request.data)
        print(a)
        a.is_valid()
        user = a.save()
        return Response(Library1Serializer(user).data)


class Book1View(generics.GenericAPIView):
    serializer_class = Book1Serializer

    def post(self, request, *args, **kwargs):
        b = Book1Serializer(data=request.data)
        b.is_valid(raise_exception=True)
        user = b.save()
        return Response(Book1Serializer(user).data)


class Get1View(generics.GenericAPIView):
    queryset = Book1Serializer

    def get(self, request):
        movies = Book.objects.all()
        serializer = Book1Serializer(movies, many=True)
        print(serializer.data)
        return Response(serializer.data)

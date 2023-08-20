from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from rest_framework.response import Response
from .serializers import LibrarySerializer, BookSerializer
from .models import *


# Create your views here.
class LibraryView(generics.GenericAPIView):
    serializer_class = LibrarySerializer

    def post(self, request, *args, **kwargs):
        a = LibrarySerializer(data=request.data)
        print(a)
        a.is_valid()
        user = a.save()
        return Response(LibrarySerializer(user).data)


class BookView(generics.GenericAPIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        b = BookSerializer(data=request.data)
        b.is_valid(raise_exception=True)
        user = b.save()
        return Response(BookSerializer(user).data)


class GetView(generics.GenericAPIView):
    queryset = BookSerializer

    def get(self, request):
        movies = Book.objects.all()
        serializer = BookSerializer(movies, many=True)
        print(serializer.data)
        return Response(serializer.data)

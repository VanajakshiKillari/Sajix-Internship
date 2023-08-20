from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import *
from .serializers import moduleSerializer,studentSerializer


class moduleAPIView(generics.GenericAPIView):
    serializer_class = moduleSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(moduleSerializer(user).data)


class studentAPIView(generics.GenericAPIView):
    serializer_class = studentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(studentSerializer(user).data)


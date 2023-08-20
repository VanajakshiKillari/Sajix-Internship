from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CreateSerializer
from .models import cruddb


class createsAPI(generics.GenericAPIView):
    serializer_class = CreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(CreateSerializer(user).data)


class Get(generics.ListAPIView):
    queryset = cruddb.objects.all()
    serializer_class = CreateSerializer


class Update(generics.UpdateAPIView):
    queryset = cruddb.objects.all()
    serializer_class = CreateSerializer


class Destroy(generics.DestroyAPIView):
    queryset = cruddb.objects.all()
    serializer_class = CreateSerializer
# Create your views here.

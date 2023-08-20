from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CreateSerializer,Create1Serializer,loginSerializer,login1Serializer
from .models import cruddb,cruddata
from rest_framework.permissions import IsAuthenticated
class createsAPI(generics.GenericAPIView):
    serializer_class = CreateSerializer
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(CreateSerializer(user).data)
class createsAPI(generics.GenericAPIView):
    serializer_class = Create1Serializer
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(Create1Serializer(user).data)
class Get(generics.ListAPIView):
    queryset = cruddb.objects.all()
    for each in queryset:
        if len(each.firstname)==6:
            print(each.firstname)
    serializer_class = CreateSerializer
    # permission_classes = (IsAuthenticated,)
class Get(generics.ListAPIView):
    queryset = cruddata.objects.all()
    serializer_class = Create1Serializer
    # permission_classes = (IsAuthenticated,)
class Update(generics.UpdateAPIView):
    queryset = cruddb.objects.all()
    serializer_class = CreateSerializer
    # permission_classes = (IsAuthenticated,)
class Update(generics.UpdateAPIView):
    queryset = cruddata.objects.all()
    serializer_class = Create1Serializer
    # permission_classes = (IsAuthenticated,)
class Destroy(generics.DestroyAPIView):
    queryset = cruddb.objects.all()
    serializer_class = CreateSerializer
    # permission_classes = (IsAuthenticated,)
class Destroy(generics.DestroyAPIView):
    queryset = cruddata.objects.all()
    serializer_class = Create1Serializer
    # permission_classes = (IsAuthenticated,)
class loginView(generics.GenericAPIView):
    serializer_class = loginSerializer
    # permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        try:
            firstname = request.data.get('firstname')
            email = request.data.get('email')
            a = cruddb.objects.get(firstname=firstname,email=email)
            if a:
                return HttpResponse("login Successful")
        except:
            return HttpResponse("login not Successful")
class loginView(generics.GenericAPIView):
    serializer_class = login1Serializer
    # permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        try:
            firstname = request.data.get('firstname')
            email = request.data.get('email')
            # phonenumber=request.data.get('phonenumber')
            a = cruddb.objects.get(firstname= firstname)
            if email == str(a.phonenumber) or email == a.email:
                return HttpResponse("login Successful")
            else:
                return HttpResponse("login not Successful")
        except:
            return HttpResponse("login not Successful")
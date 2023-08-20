from rest_framework import serializers
from .models import cruddb,cruddata
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = cruddb
        fields = '__all__'
class getByIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = cruddb
        fields = ['firstname','email']
class Create1Serializer(serializers.ModelSerializer):
    class Meta:
        model = cruddata
        fields = '__all__'
class getByIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
class login1Serializer(serializers.ModelSerializer):
    class Meta:
        model=cruddata
        fields=['username','password']
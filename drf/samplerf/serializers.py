from rest_framework import serializers
from .models import cruddb
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
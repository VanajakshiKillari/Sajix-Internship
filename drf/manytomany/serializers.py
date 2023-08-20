from rest_framework import serializers
from .models import *


class moduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = modules
        fields = ['id', 'module_name', 'module_duration', 'class_room']


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['id', 'name', 'age', 'grade', 'modules']
from rest_framework import serializers
from .models import Library, Book


class Library1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class Book1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
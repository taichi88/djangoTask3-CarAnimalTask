from . models import Animal

from rest_framework import serializers


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['name','species','age','is_endangered'] #or we can write '__all__" magitmethod and it will take all fields from models
        

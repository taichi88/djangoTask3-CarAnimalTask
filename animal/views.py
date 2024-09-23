from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Animal
from . serializers import AnimalSerializer

class SelectAnimalView(APIView):
    def get(self, request):
        data = Animal.objects.all()
        serializer = AnimalSerializer(data, context={'request':request}, many=True)
        return Response(serializer.data)
    

class AddAnimalView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class DeleteAnimalVIew(APIView):
    def delete(self, request, pk):
        event = Animal.objects.get(pk=pk)
        event.delete()
        return Response("Delettion is succesfull")
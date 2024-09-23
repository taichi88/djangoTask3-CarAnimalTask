from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Car
from . serializers import CarSerializer

class SelectCarView(APIView):
    def get(self, request, pk=None):
        if pk: #ეს კოდი განსხახავდება ანიმალის კოდისგან, ვინაიდან ამის მიხედვით, ჩვენს თU გაქვს 4 ჩანაწერი, და URL ში მივუთითებს მაგალითად 1-ს ის გვაჩვენებს პირველ ჩანაწერს. 
            try:
                data = Car.objects.get(pk=pk)
                serializer = CarSerializer(data, context={'request':request}, many=False)
                return Response(serializer.data)
            except:
                return Response("COuld not find a car whit id - " + str(pk))
        data = Car.objects.all()
        serializer = CarSerializer(data, context={"request":request},many=True)
        return Response(serializer.data)

class AddCarView(APIView):
    def post(self, request):
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class DeleteCarVIew(APIView):
    def delete(self, request, pk):
        event = Car.objects.get(pk=pk)
        event.delete()
        return Response("Delettion is succesfull")
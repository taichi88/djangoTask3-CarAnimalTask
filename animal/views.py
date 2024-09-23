from django.shortcuts import render, redirect
from .forms import AnimalForm
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Animal
from . serializers import AnimalSerializer


def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_urls')  # Redirect after successful save
    else:
        form = AnimalForm()
    
    return render(request, 'animal/add_animal.html', {'form': form})

def success(request):
    return HttpResponse("The animal has succecssfully added!!!")

class SelectAnimalView(APIView):
    def get(self, request):
        data = Animal.objects.all()
        serializer = AnimalSerializer(data, context={'request':request}, many=True)
        return Response(serializer.data)





from django.shortcuts import render, redirect
from .forms import CarForm

# Create your views here.

def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Replace with your success URL
    else:
        form = CarForm()
    
    return render(request, 'add_car.html', {'form': form})

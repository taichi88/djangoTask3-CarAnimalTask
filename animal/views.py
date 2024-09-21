from django.shortcuts import render, redirect
from .forms import AnimalForm

def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect after successful save
    else:
        form = AnimalForm()
    
    return render(request, 'add_animal.html', {'form': form})

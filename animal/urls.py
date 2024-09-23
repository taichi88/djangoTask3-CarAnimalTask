from django.urls import path
from . import views




urlpatterns = [
    path('add_animal/', views.add_animal ),
    path('success/', views.success, name='success_urls'),
    path('select_animal/', views.SelectAnimalView.as_view(), name="SelectAllAnimals")


]

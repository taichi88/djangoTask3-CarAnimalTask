from django.urls import path
from . import views




urlpatterns = [
    path('add_animal/', views.AddAnimalView.as_view(), name='AddAnimals'),
    path('', views.SelectAnimalView.as_view(), name="SelectAllAnimals"),
    path('delete_animal/<int:pk>/', views.DeleteAnimalVIew.as_view(), name="DeleteAnimal")

]

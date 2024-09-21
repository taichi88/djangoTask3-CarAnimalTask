from django.urls import path
from . import views



urlpatterns = [
    path('animal/', views.add_animal, name='add_animal'),
]

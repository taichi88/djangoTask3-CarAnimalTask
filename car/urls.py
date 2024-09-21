
from django.urls import path
from . import views



urlpatterns = [

    path('car/', views.add_car, name='add_car'),
    

]

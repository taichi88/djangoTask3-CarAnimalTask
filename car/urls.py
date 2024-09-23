
from django.urls import path
from . import views



urlpatterns = [

    
    path('add_car/', views.AddCarView.as_view(), name='AddCar'),
    path('<int:pk>/', views.SelectCarView.as_view(), name="SelectOneCar"),

    path('', views.SelectCarView.as_view(), name="SelectAllCar"),
    path('delete_Car/<int:pk>/', views.DeleteCarVIew.as_view(), name="DeleteCar")

    

]

from django.db import models

# Create your models here.


class Car(models.Model):
    # Basic Information
    make = models.CharField(max_length=50)  # Manufacturer (e.g., Toyota, Ford)
    model = models.CharField(max_length=50)  # Model name (e.g., Corolla, Mustang)
    year = models.PositiveIntegerField()  # Year of manufacture
    color = models.CharField(max_length=30)  # Color of the car

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.color})"
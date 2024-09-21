from django.db import models

# Create your models here.


class Animal(models.Model):

    name = models.CharField(max_length=100)  # Name of the animal
    species = models.CharField(max_length=50)  # Species (e.g., dog, cat, bird)
    age = models.PositiveIntegerField()  # Age
    is_endangered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} ({self.species})"
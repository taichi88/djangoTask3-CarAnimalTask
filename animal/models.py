from django.db import models

# Create your models here.


class Book(models.Model):
    title  = models.CharField(default='book', max_length=100)
    
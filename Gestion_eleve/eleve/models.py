from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    naissance = models.CharField(max_length=15)
    sexe = models.CharField(max_length=10)
    niveau = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

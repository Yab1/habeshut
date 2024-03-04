from enum import unique
from django.db import models


# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    phone = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to="agents/")
    about = models.CharField(max_length=500)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20)


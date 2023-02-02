from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    phone_number = models.CharField(max_length=20)

  

    class Meta:
        verbose_name_plural = ('Users')
        verbose_name = ("User")
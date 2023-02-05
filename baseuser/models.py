from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    bio = models.TextField(blank= True)
    image = models.ImageField(upload_to='users/', blank=True)

    class Meta:
        verbose_name_plural = ('Users')
        verbose_name = ("User")
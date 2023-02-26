from django.db import models
# from baseuser.forms import User
# from django.contrib.auth import get_user_model
# User = get_user_model()

from core.models import AbstractBaseModel

# Create your models here.
class News(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/homepage1')
    author = models.CharField(max_length=100)
       # slug = models.SlugField(max_length=100,editable=False)


    class Meta:
        verbose_name_plural = "News"
        verbose_name = "News"

    def __str__(self): 
        return self.title

    
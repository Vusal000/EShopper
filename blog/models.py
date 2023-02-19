from django.db import models
from baseuser.forms import User

from core.models import AbstractBaseModel

# Create your models here.
class News(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='media/homepage1')
    author = models.ForeignKey(User, on_delete=models.CASCADE)    # slug = models.SlugField(max_length=100,editable=False)


    class Meta:
        verbose_name_plural = "News"
        verbose_name = "News"

    def __str__(self): 
        return self.title

    
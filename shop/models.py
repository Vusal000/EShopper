from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractBaseModel):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"
        verbose_name = "Category"

    def __str__(self): 
        return self.title

class Color(AbstractBaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
       return self.title

class Size(AbstractBaseModel):
    title = models.CharField(max_length=10)

    def __str__(self):
       return self.title

class Products(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='media/homepage1')
    price = models.FloatField(max_length=100)
    compared_price = models.FloatField(max_length=10,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    slug = models.SlugField( null=False, blank=True, unique=True, db_index=True ,  editable=False)

    def __str__(self):
       return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('shopdetails', kwargs={'slug': self.slug})

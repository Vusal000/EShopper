from django.db import models



# Create your models here.

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class category(AbstractBaseModel):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"
        verbose_name = "Category"

    def __str__(self): 
        return self.title



class Products(AbstractBaseModel):
    title1 = models.CharField(max_length=100)
    description2 = models.TextField(max_length=200)
    image1 = models.ImageField(upload_to='media/homepage1')

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Products"

    def __str__(self): 
        return self.title1
    
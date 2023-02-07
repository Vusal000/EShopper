from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class contact(AbstractBaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    # is_check = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Contact"
        verbose_name = "Contact"

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.is_check = True
        super(contact, self).save(*args,**kwargs)


class settings(AbstractBaseModel):
    logo = models.ImageField(upload_to='media/logo')
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Settings"
        verbose_name = "Setting"


    def __str__(self):
        return "My Site Settings"



class subscribe(AbstractBaseModel):
    email = models.EmailField(max_length=100)


    class Meta:
        verbose_name_plural = "Subscribers"
        verbose_name = "Subscriber"

    def __str__(self):
        return self.email

class homepage(AbstractBaseModel):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    description1 = models.TextField(max_length=200)
    description2 = models.TextField(max_length=200)
    image1 = models.ImageField(upload_to='media/homepage1')
    image2 = models.ImageField(upload_to='media/homepage2')

    class Meta:
        verbose_name_plural = "Homepage"
        verbose_name = "Homepage"

    def __str__(self): 
        return self.title1
    
class category(AbstractBaseModel):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"
        verbose_name = "Category"

    def __str__(self): 
        return self.title

class blog(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='media/product')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Blog"
        verbose_name = "Blog"

    def __str__(self):
        return self.title

class advertisement(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'media/advertisement')
    
    class Meta:
        verbose_name_plural = "Advertisements"
        verbose_name = "Advertisement"

    def __str__(self):
        return self.title




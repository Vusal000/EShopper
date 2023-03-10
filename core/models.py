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


class Settings(AbstractBaseModel):
    logo = models.ImageField(upload_to='media/logo')
    image1 = models.ImageField(upload_to='media/image1')
    information1 = models.TextField()
    description1 = models.TextField()
    image2 = models.ImageField(upload_to='media/image2')
    information2 = models.TextField()
    description2 = models.TextField()
    location = models.CharField(max_length=100)
    about_us = models.TextField()
    button = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedln = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    

    class Meta:
        verbose_name_plural = "Settings"
        verbose_name = "Setting"


    def __str__(self):
        return "My Site Settings"



class subscribe(AbstractBaseModel):
    email = models.EmailField(max_length=100, unique=True, db_index=True)

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
    



class advertisement(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to = 'media/advertisement')
    
    class Meta:
        verbose_name_plural = "Advertisements"
        verbose_name = "Advertisement"

    def __str__(self):
        return self.title



# class News(AbstractBaseModel):
#     title = models.CharField(max_length=100)
#     description = models.TextField(max_length=200)
#     image = models.ImageField(upload_to='media/homepage1')
#     # slug = models.SlugField(max_length=100,editable=False)


#     class Meta:
#         verbose_name_plural = "News"
#         verbose_name = "News"

#     def __str__(self): 
#         return self.title

    
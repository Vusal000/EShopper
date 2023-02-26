from django.contrib import admin

# Register your models here.
from .models import  Category, Color, Products, Size


admin.site.register(Category)
admin.site.register(Products)

admin.site.register(Color)
admin.site.register(Size)



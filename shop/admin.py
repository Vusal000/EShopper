from django.contrib import admin

# Register your models here.
from .models import category,Products


admin.site.register(category)
admin.site.register(Products)


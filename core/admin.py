from django.contrib import admin

# Register your models here.

from .models import  Settings, advertisement, contact, subscribe, category, blog, homepage

admin.site.register(contact)
admin.site.register(Settings)
admin.site.register(subscribe)
admin.site.register(homepage)
admin.site.register(category)
admin.site.register(blog)
admin.site.register(advertisement)
# admin.site.register(News)


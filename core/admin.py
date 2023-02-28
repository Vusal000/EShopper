from django.contrib import admin

# Register your models here.

from .models import  Settings, advertisement, contact, subscribe, homepage

admin.site.register(contact)
admin.site.register(Settings)
admin.site.register(subscribe)
admin.site.register(homepage)
admin.site.register(advertisement)
# admin.site.register(News)


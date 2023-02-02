from django.contrib import admin

# Register your models here.

from .models import advertisement, contact, settings, subscribe, category, blog, homepage

admin.site.register(contact)
admin.site.register(settings)
admin.site.register(subscribe)
admin.site.register(homepage)
admin.site.register(category)
admin.site.register(blog)
admin.site.register(advertisement)


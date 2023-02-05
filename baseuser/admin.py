from django.contrib import admin
from .models import MyUser
# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    # list_display = ('username', 'email', 'bio','image')
    # list_display_links = ('username', 'email')
    search_fields = ('username', 'email')
    last_filter = ('username', 'email')
    list_per_page = 25 

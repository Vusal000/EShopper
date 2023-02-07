from django.contrib import admin
from .models import MyUser
# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'bio')
    search_fields = ('username', 'email')
    last_filter = ('username', 'email')

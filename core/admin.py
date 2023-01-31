from django.contrib import admin

# Register your models here.

from .models import contact

# admin.site.register(contact)


@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'is_check')
    list_filter = ('is_check',)
    search_fields = ('name',)
    readonly_fields = ('email','text')


    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'email'),
            'classes': ('collapse'),
        }),
        ('Additional info', {
            'fields': ('text', 'is_check')
        }),
    )
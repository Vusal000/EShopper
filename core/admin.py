from django.contrib import admin

# Register your models here.

from .models import advertisement, contact,settings,Subscibers,homepage,category,product,blog

# admin.site.register(contact)
# admin.site.register(settings)
admin.site.register(Subscibers)
admin.site.register(homepage)
admin.site.register(product)
admin.site.register(category)
admin.site.register(blog)
admin.site.register(advertisement)



@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','is_check')
    list_filter = ('is_check',)
    search_fields = ('name','email')
    readonly_fields = ('email',)

    fieldsets = (
        ('Personal info',{
            'fields' : ('name', 'email')
        }),
        ('Additional info', {
            'fields': ('text','is_check')
        }),
    )

@admin.register(settings)
class SettingsAdmin(admin.ModelAdmin):
    

    def has_delete_permission(self, request,obj = None):
        return False
    
    def has_change_permission(self, request,obj = None):
        return False
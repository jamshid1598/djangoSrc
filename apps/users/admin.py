from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUserModel


# Register your models here.


class CustomUserAdmin(BaseUserAdmin):
    list_display=('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
    list_display_links=('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'created_at', 'updated_at')
    list_dialects=('username', 'first_name', 'last_name', 'middle_name')
    search_fields=('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone_number')
    list_filter=('is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
    filter_horizontal=()
    
    fieldsets=(
        ('User Info', {
            'fields': (
                'image',
                'username',
                'first_name',
                'last_name',
                'middle_name',
                'email',
                'phone_number',
            )
        }),
        ('Status/Groups/Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )
    
    add_fieldsets = (
        ('Create New User', {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'phone_number',
                'password1',
                'password2',
            )
        }),
    )
    
    
    
    
admin.site.register(CustomUserModel, CustomUserAdmin)
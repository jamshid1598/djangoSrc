from django.contrib import admin
from django.utils.text import slugify
from .models import (
    Category,
    Post,
)

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display       = ('name', 'created_at', 'updated_at')
    list_display_links = ('name',)
    search_fields      = ('name',)
    ordering           = ('name', 'created_at', 'updated_at',)
    list_filter        = ('created_at', 'updated_at',)
    readonly_fields    = ('slug',)
    
    # prepopulated_fields = {'slug': ('name', )}
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
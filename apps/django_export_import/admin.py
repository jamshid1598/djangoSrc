from django.contrib import admin
from import_export import resources, fields

from .models import (
    Author,
    Category,
    Book,
)

# Register your models here.

class BookResource(resources.ModelResource):
    published = fields.Field(attribute='published', column_name='published_name')
    class Meta:
        model=Book
        fields = ('name', 'author__name', 'author_email', 'published', 'price', 'categories__name')
        exclude = ('imported',)
        export_order = ('categories__name', 'name', 'author__name', 'author_email', 'published', 'price',)


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
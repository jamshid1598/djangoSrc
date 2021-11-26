from django.contrib import admin
from import_export import resources, fields
from import_export.admin import (
    ImportExportModelAdmin, 
    ImportExportActionModelAdmin,
    
    ExportMixin,
    ImportMixin,
    ImportExportMixin,
    
    ExportActionMixin,
    ExportActionModelAdmin,
)

from .models import (
    Author,
    Category,
    Book,
)
from .forms import (
    BookImportForm,
    CustomConfirmImportForm,
)
# Register your models here.

class BookResource(resources.ModelResource):
    published = fields.Field(attribute='published', column_name='published_date')
    extra_column = fields.Field(column_name='extra-column')
    full_title = fields.Field()
    # class Meta:
    #     model=Book
    #     fields = ('name', 'author__name', 'author_email', 'published', 'price', 'categories__name')
    #     exclude = ('imported',)
    #     export_order = ('categories__name', 'name', 'author__name', 'author_email', 'published', 'price',)
    class Meta:
        model=Book
        fields = ('id', 'author_email', 'published', 'price', 'categories')
        exclude = ('imported',)
        export_order = ('id', 'categories', 'full_title', 'author_email', 'published', 'price',)
        widgets = {
            'published_date': {'format': '%d.%m.%Y'},
        }
        
    def dehydrate_full_title(self, book):
        return f"{book.name} by {book.author.name}"


class BookAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = BookResource

    list_display = ('name', 'author', 'author_email', 'published', 'price',)
    # pass
    
    def get_import_form(self):
        return BookImportForm
    
    def get_confirm_import_form(self):
        return CustomConfirmImportForm
    
    def get_form_kwargs(self, form, *args, **kwargs):
        if isinstance(form, CustomConfirmImportForm):
            if form.is_vlid():
                author = form.cleaned_data.get('author')
                kwargs.update({'author': author.id})
        return kwargs
    
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)
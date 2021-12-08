from django.contrib import admin
from import_export.admin import (
    ImportExportModelAdmin, 
    ImportExportActionModelAdmin,
)

from .models import (
    Author,
    Category,
    Book,
)
from .resources import (
    BookResource,
)
from .forms import (
    BookImportForm,
    CustomConfirmImportForm,
)

# Register your models here.


class BookAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
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
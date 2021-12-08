from import_export import (
    resources,
    fields,
    widgets,
)
from .widgets import (
    DateWidget,
    DateTimeWidget,
    ForeignKeyWidget,
    ManyToManyWidget,
)
from .models import (
    Author,
    Category,
    Book,
)


class BookResource(resources.ModelResource):
    published = fields.Field(attribute='published', column_name='published at', widget=DateWidget(format="%d-%m-%Y"))
    author    = fields.Field(attribute='author', column_name='Auther', widget=ForeignKeyWidget(Author, 'name'))
    categories  = fields.Field(attribute='categories', column_name='Categories', widget=ManyToManyWidget(Category, 'name'))
    full_title = fields.Field()
   
    class Meta:
        model=Book
        fields = ('id', 'author', 'author_email', 'published', 'price', 'categories')
        exclude = ('imported',)
        export_order = ('id', 'categories', 'full_title', 'author', 'author_email', 'published', 'price',)
        widgets = {
            'published_date': {'format': '%d.%m.%Y'},
        }
        
    def dehydrate_full_title(self, book):
        try:
            return f"{book.name} by {book.author.name}" 
        except:
            return "%s by %s"%(book.name, "unknown")
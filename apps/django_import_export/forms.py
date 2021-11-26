from django import forms
from import_export.forms import ImportForm, ConfirmImportForm
from .models import (
    Author,
    Category,
    Book,
)

class BookImportForm(ImportForm):
    author = forms.ModelChoiceField(queryset = Author.objects.all(), required=True,)

class CustomConfirmImportForm(ConfirmImportForm):
    author = forms.ModelChoiceField(queryset = Author.objects.all(), required=True)
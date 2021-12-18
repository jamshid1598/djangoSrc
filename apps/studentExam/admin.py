from django.contrib import admin
from import_export.admin import (
    ImportExportModelAdmin, 
    ImportExportActionModelAdmin,
)

from .models import (
   Student,
)
from .resources import (
    StudentResource,
)


# Register your models here.


class StudentAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    resource_class = StudentResource
    list_display = ('id', 'f_name', 'l_name', 'm_name', 'group', 'direction')
    
admin.site.register(Student, StudentAdmin)

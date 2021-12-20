from django.contrib import admin
from import_export.admin import (
    ImportExportModelAdmin, 
    ImportExportActionModelAdmin,
)

from .models import (
   TestDB,
   Student,
)
from .resources import (
    TestDBResource,
    StudentResource,
)


# Register your models here.


class StudentAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    resource_class = StudentResource
    list_display = ('id', 'f_name', 'l_name', 'm_name', 'group', 'direction')
    
admin.site.register(Student, StudentAdmin)


class TestDBAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    resource_class = TestDBResource
    list_display = ('id', 'q')
    
admin.site.register(TestDB, TestDBAdmin)
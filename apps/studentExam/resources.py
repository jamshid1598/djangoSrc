from import_export import (
    resources,
    fields,
    widgets,
)
# from .widgets import (
#     DateWidget,
#     DateTimeWidget,
#     ForeignKeyWidget,
#     ManyToManyWidget,
# )
from .models import (
   Student,
)


class StudentResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='№')
    l_name = fields.Field(attribute='l_name', column_name='Фамилия')
    f_name = fields.Field(attribute='f_name', column_name='Исми')
    m_name = fields.Field(attribute='m_name', column_name='Шарифи')

    group = fields.Field(attribute='group', column_name='Группа')
    direction = fields.Field(attribute='direction', column_name='Йўналиш')

    fan1 = fields.Field(attribute='fan1', column_name='Фан1')
    fan2 = fields.Field(attribute='fan2', column_name='Фан2')
    fan3 = fields.Field(attribute='fan3', column_name='Фан3')
    fan4 = fields.Field(attribute='fan4', column_name='Фан4')
    fan5 = fields.Field(attribute='fan5', column_name='Фан5')
    fan6 = fields.Field(attribute='fan6', column_name='Фан6')
    fan7 = fields.Field(attribute='fan7', column_name='Фан7')
    fan8 = fields.Field(attribute='fan8', column_name='Фан8')
    fan9 = fields.Field(attribute='fan9', column_name='Фан9')
    fan10 = fields.Field(attribute='fan10', column_name='Фан10')
    fan11 = fields.Field(attribute='fan11', column_name='Фан11')
    fan12 = fields.Field(attribute='fan12', column_name='Фан12')
    fan13 = fields.Field(attribute='fan13', column_name='Фан13')
    fan14 = fields.Field(attribute='fan14', column_name='Фан14')
    fan15 = fields.Field(attribute='fan15', column_name='Фан15')
    fan16 = fields.Field(attribute='fan16', column_name='Фан16')
    fan17 = fields.Field(attribute='fan17', column_name='Фан17')
    fan18 = fields.Field(attribute='fan18', column_name='Фан18')
    fan19 = fields.Field(attribute='fan19', column_name='Фан19')
    fan20 = fields.Field(attribute='fan20', column_name='Фан20')

   
    class Meta:
        model=Student
        fields = (
            "id", "l_name", "f_name", "m_name", "group", "direction",
            "fan1","fan2","fan3","fan4","fan5","fan6","fan7","fan8","fan9","fan10",
            "fan11","fan12","fan13","fan14","fan15","fan16","fan17","fan18","fan19","fan20",
        )
        export_order = (
            "id", "l_name", "f_name", "m_name", "group", "direction",
            "fan1","fan2","fan3","fan4","fan5","fan6","fan7","fan8","fan9","fan10",
            "fan11","fan12","fan13","fan14","fan15","fan16","fan17","fan18","fan19","fan20",
        )
    
    def before_import_row(self, row, row_number=None, **kwargs):
        
        pass
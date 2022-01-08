from projectroot.settings.base import *



# Override default project settings

#  tinymce configuration
TINYMCE_DEFAULT_CONFIG = {
    'height': 400, 
    'width': 800, 
    'cleanup_on_startup': True, 
    'custom_undo_redo_levels': 20, 
    'selector': 'textarea', 
    'theme': 'modern', 
    'plugins': ''' textcolor save link image media preview codesample contextmenu 
                   table code lists fullscreen insertdatetime nonbreaking contextmenu 
                   directionality searchreplace wordcount visualblocks visualchars 
                   code fullscreen autolink lists charmap print hr anchor pagebreak ''', 
    'toolbar1': ''' fullscreen preview bold italic underline | fontselect, fontsizeselect | 
                    forecolor backcolor | alignleft alignright | aligncenter alignjustify | 
                    indent outdent | bullist numlist table | | link image media | codesample | ''', 
    'toolbar2': ''' visualblocks visualchars | charmap hr pagebreak nonbreaking anchor | code | ''', 
    'contextmenu': 'formats | link image', 
    'menubar': True, 
    'statusbar': True, 
}


# DJANGO-REST-FRAMEWORK configurations
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.DjangoModelPermissions',
    ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':5,
}




try:
    from projectroot.settings.local import *
except:
    print("if project is on development progress, than you should create local.py file for local settings")



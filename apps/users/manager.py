from django.utils.translation import gettext_lazy as _




class CustomUserManager():
    
    def _create_user(request, username, *args, **kwargs):
        
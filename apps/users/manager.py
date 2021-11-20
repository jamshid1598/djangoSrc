from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _




class CustomUserManager(BaseUserManager):    
    def _create_user(self, username, password, email, phone_number, is_staff, is_superuser, **kw_extra_fields):
        if not username:
            raise ValueError(_("username must be provided"))
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            phone_number=phone_number,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **kw_extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, email, phone_number, **kw_extra_fields):
        return self._create_user(username, password, email, phone_number, False, False, **kw_extra_fields)
    
    def create_superuser(self, username, password, email, phone_number, **kw_extra_fields):
        return self._create_user(username, password, email, phone_number, True, True, **kw_extra_fields)
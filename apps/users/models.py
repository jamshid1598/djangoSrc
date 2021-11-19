from django.db import models
from django.urls import reverse
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser 
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
import uuid

from .manager import CustomUserManager



class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    user_id      = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    image        = models.ImageField(_("Image"), upload_to='image/user/', blank=True, null=True)
    username     = models.CharField(_("Username"), max_length=200, unique=True, )
    first_name   = models.CharField(_("First Name"), max_length=200, blank=True, null=True)
    second_name  = models.CharField(_("Second Name"), max_length=200, blank=True, null=True)
    third_name   = models.CharField(_("Third Name"), max_length=200, blank=True, null=True)
    phone_number = PhoneNumberField(_("Phone Number"), blank=True, null=True)
    email        = models.EmailField(_("Email"), blank=True, null=True)
    
    created_at = models.DateField(_("Created at"), auto_add_now=True)
    updated_at = models.Datefield(_("Updated at"), auto_add=True)
    
    is_active    = models.BooleanField("is active", default=False)
    is_staff     = models.BooleanField("is staff", default=False)
    is_superuser = models.BooleanField("is superuser", default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number', 'email',]
    
    class Meta:
        ordering = ['username', 'created_at', 'updated_at']
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        # return reverse("user:user-detail", kwargs={"user_id": self.user_id})
        return "user/%si/" % (self.user_id)
     
    @property
    def image(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url




from django.urls import path, include
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import routers

from .views import (
    UserViewSet,
    GroupViewSet,
)

app_name='drf'


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
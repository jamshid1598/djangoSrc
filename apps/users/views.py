from django.shortcuts import render
from rest_framework import (
    viewsets,
    permissions,
)
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


from .serializers import (
    UserSerializer, 
    GroupSerializer,
)


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
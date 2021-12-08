from django.urls import path, include
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import (
    routers, 
    serializers, 
    viewsets,
)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=[
            'url'
            'user_id'
            'username',
            'image',
            'first_name',
            'last_name',
            'middle_name',
            'phone_number',
            'email',
            
            'created_at',
            'updated_at',
        ]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


app_name='drf'




urlpatterns = [
    path('', include(router.urls ))
]
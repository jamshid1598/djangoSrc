from rest_framework import (
    serializers,
    generics,
)

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()



class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_field="user_id", view_name="users:user-detail")
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        

from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers

from .models import (
    LANGUAGE_CHOICES,
    STYLE_CHOICES,
    LEXERS,
)
from .models import (
    Snippet,
)


class UserModelSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model =User
        fields = ['user_id', 'username', 'snippets']


class SnippetHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        lookup_field='id',
        view_name="drf:snippet-detail-update-delete-v5")
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        lookup_field = "id",
        view_name="drf:snippet-highlighted", format="html")

    class Meta:
        model = Snippet
        fields = ["url", "id", "owner",  "highlight", "title", "code", "linenos", "language", "style", "created"]


class UserHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        lookup_field='user_id', 
        view_name="users:customusermodel-detail")
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail-update-delete-v5', read_only=True)
    class Meta:
        model=User
        fields = ['url', "user_id", "username", "snippets"]


class SnippetModelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = [ 'owner', 'id', 'title', 'code', 'linenos', 'language', 'style',]

class SnippetSerializer(serializers.Serializer):
    id        = serializers.IntegerField(read_only=True)
    title     = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code      = serializers.CharField(style={"base_template": "textarea.html"})
    linenos   = serializers.BooleanField(required=False)
    language  = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style     = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        update and return an existing 'Snippet' instance, given the validated data 
        """
        instance.title    = validated_data.get('title', instance.title)
        instance.code     = validated_data.get('code', instance.code)
        instance.linenos  = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style    = validated_data.get('style', instance.style)
        instance.save()
        
        return instance
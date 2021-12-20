from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import (
    mixins,
    generics,
    viewsets,
    permissions,
    status,
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from django.http import (
    Http404,
    HttpResponse,
    JsonResponse,
)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Snippet
from .serializers import (
    SnippetSerializer,
    SnippetModelSerializer,
    UserSnippetSerializer,
)
from .permissions import (
    IsOwnerOrReadOnly,
)
# Create your views here.


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users":reverse("drf:user-snippet-list-v1", request=request, format=format),
        "snippets":reverse("drf:snippet-list-v5", request=request, format=format),
    })





@csrf_exempt
def snippet_list_create_v1(request):
    """
    list all code snippets or create new one
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse9(request)
        serializer = SnippetModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def snippet_list_create_v2(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SnippetModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def snippet_detail_v1(request, id):
    
    try:
        snippet = Snippet.objects.get(id=id)
    except:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetModelSerializer(snippet)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetModelSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail_v2(request, id, format=None):
    try:
        snippet = Snippet.objects.get(id=id)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        # return Http404
    
    if request.method == 'GET':
        serializer = SnippetModelSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = SnippetModelSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
        APIView class based list/create view 
"""
class SnippetListCreateAPIView(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = SnippetModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
        APIView class based detail view 
"""
class SnippetDetailUpdateDeleteAPIView(APIView):
    def get_object(self, id):
        try:
            return Snippet.objects.get(id=id)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = SnippetModelSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = SnippetModelSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
        Mixin class based list view 
"""
class SnippetListCreateMixinView(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class SnippetDetailUpdateDeleteMixinView(mixins.RetrieveModelMixin,
                                         mixins.UpdateModelMixin,
                                         mixins.DestroyModelMixin,
                                         generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""
        Generic class based views
"""
class SnippetListCreateGenericApiView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetailUpdateDeleteGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'



"""
        Authentication and Permissions
"""
class UserSnippetlistApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSnippetSerializer
    
    
class UserSnippetDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSnippetSerializer
    lookup_field = 'user_id'

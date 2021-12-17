from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import (
    viewsets,
    permissions,
    status,
)
from rest_framework.response import Response
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
from .serializers import SnippetModelSerializer

# Create your views here.

@csrf_exempt
def snippet_list_v1(request):
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
def snippet_list_v2(request, format=None):
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




class SnippetListAPIView(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = SnippetModelSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import (
    viewsets,
    permissions,
)
from .models import Snippet
from .serializers import SnippetModelSerializer

# Create your views here.

@csrf_exempt
def snippet_list(request):
    """
    list all code snippets or create new one
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = SnippetModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, id):
    
    try:
        snippet = Snippet.objects.get(id=id)
    except:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetModelSerializer(snippet)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = SnippetModelSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
        
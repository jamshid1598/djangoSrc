from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.




class HomeView(View):
    template_name='htmx/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {'status':'success'})


class ListView(View):
    template_name='htmx/list.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class DetailView(View):
    template_name='htmx/detail.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class CreateView(View):
    template_name='htmx/create.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class UpdateView(View):
    template_name='htmx/update.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class DeleteView(View):
    template_name='htmx/delete.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


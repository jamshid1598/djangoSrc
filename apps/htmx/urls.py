from django.urls import path

from .views import (
    HomeView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

app_name="htmx"

urlpatterns = [
    path("",        HomeView.as_view(),   name='home'),
    path("list/",   ListView.as_view(),   name='list'),
    path("detail/", DetailView.as_view(), name='detail'),
    path("create/", CreateView.as_view(), name='create'),
    path("update/", UpdateView.as_view(), name='update'),
    path("detail/", DeleteView.as_view(), name='delete'),
]
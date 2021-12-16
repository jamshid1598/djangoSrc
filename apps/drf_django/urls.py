from django.urls import path, include
from rest_framework import routers
from .views import snippet_list

app_name='drf'

# router = routers.DefaultRouter()
# router.register(r"snippet", snippet_list)


urlpatterns = [
    # path('', include(router.urls)),
    path("snippet-list/", snippet_list, name='snippet-list'),
]
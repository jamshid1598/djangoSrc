from django.urls import path
from .views import import_func

app_name = "import"


urlpatterns = [
    path("", import_func, name="import"),
]

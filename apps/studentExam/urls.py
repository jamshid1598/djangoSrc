from django.urls import path
from .views import import_func, read_txt

app_name = "import"


urlpatterns = [
    path("", import_func, name="import"),
    path("txt/", read_txt, name="import-txt"),
]

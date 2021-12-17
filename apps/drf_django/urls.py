from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    snippet_list_v1,
    snippet_list_v2,
    snippet_detail_v1,
    snippet_detail_v2,
)

app_name='drf'

# router = routers.DefaultRouter()
# router.register(r"snippet", snippet_list)


urlpatterns = [
    # path('', include(router.urls)),
    path("snippet-list/v1/", snippet_list_v1, name='snippet-list-v1'),
    path('snippet-list/v2/', snippet_list_v2, name='snippet-list-v2'),
    path("snippet-detail/v1/<int:id>/", snippet_detail_v1, name="snippet-detail-v1"),
    path("snippet-detail/v2/<int:id>/", snippet_detail_v2, name="snippet-detail-v2"),
]
urlpatterns = format_suffix_patterns(urlpatterns) 
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    api_root,
    SnippetHighlighted,
    
    snippet_list_create_v1,
    snippet_list_create_v2,
    snippet_detail_v1,
    snippet_detail_v2,
    
    SnippetListCreateAPIView,
    SnippetDetailUpdateDeleteAPIView,
    
    SnippetListCreateMixinView,
    SnippetDetailUpdateDeleteMixinView,
    
    SnippetListCreateGenericApiView,
    SnippetDetailUpdateDeleteGenericApiView,

    UserSnippetlistApiView,
    UserSnippetDetailApiView,    
)

app_name='drf'

# router = routers.DefaultRouter()
# router.register(r"snippet", snippet_list)


urlpatterns = [
    # path('', include(router.urls)),

    path("", api_root, name="api-root"),
    path("snippet/<int:id>/highlighted/", SnippetHighlighted.as_view(), name="snippet-highlighted"),

    path("snippet-list/v1/", snippet_list_create_v1, name='snippet-list-v1'),
    path("snippet-create/v1/", snippet_list_create_v1, name='snippet-create-v1'),
    path("snippet-detail/v1/<int:id>/", snippet_detail_v1, name="snippet-detail-v1"),
    path("snippet-update/v1/<int:id>/", snippet_detail_v1, name="snippet-update-v1"),
    path("snippet-delete/v1/<int:id>/", snippet_detail_v1, name="snippet-delete-v1"),
    
    path('snippet-list/v2/', snippet_list_create_v2, name='snippet-list-v2'),
    path('snippet-create/v2/', snippet_list_create_v2, name='snippet-create-v2'),
    path("snippet-detail/v2/<int:id>/", snippet_detail_v2, name="snippet-detail-v2"),

    path("snippet-update/v2/<int:id>/", snippet_detail_v2, name="snippet-update-v2"),
    path("snippet-delete/v2/<int:id>/", snippet_detail_v2, name="snippet-delete-v2"),
    
    path('snippet-list/v3/', SnippetListCreateAPIView.as_view(), name="snippet-list-v3"),
    path('snippet-create/v3/', SnippetListCreateAPIView.as_view(), name="snippet-create-v3"),
    path("snippet-create/v3/<int:id>/", SnippetDetailUpdateDeleteAPIView.as_view(), name="snippet-detail-v3"),
    path("snippet-update/v3/<int:id>/", SnippetDetailUpdateDeleteAPIView.as_view(), name="snippet-update-v3"),
    path("snippet-delete/v3/<int:id>/", SnippetDetailUpdateDeleteAPIView.as_view(), name="snippet-delete-v3"),

    path('snippet-list/v4/', SnippetListCreateMixinView.as_view(), name="snippet-list-v4"),
    path('snippet-create/v4/', SnippetListCreateMixinView.as_view(), name="snippet-create-v4"),
    path('snippet-detail/v4/<int:id>/', SnippetDetailUpdateDeleteMixinView.as_view(), name="snippet-detail-v4"),
    path('snippet-update/v4/<int:id>/', SnippetDetailUpdateDeleteMixinView.as_view(), name="snippet-update-v4"),
    path('snippet-delete/v4/<int:id>/', SnippetDetailUpdateDeleteMixinView.as_view(), name="snippet-delete-v4"),
    
    path('snippet-list/v5/', SnippetListCreateGenericApiView.as_view(), name="snippet-list-v5"),
    path('snippet-create/v5/', SnippetListCreateGenericApiView.as_view(), name="snippet-create-v5"),
    path('snippet-detail/v5/<int:id>/', SnippetDetailUpdateDeleteGenericApiView.as_view(), name="snippet-detail-v5"),
    path('snippet-update/v5/<int:id>/', SnippetDetailUpdateDeleteGenericApiView.as_view(), name="snippet-update-v5"),
    path('snippet-delete/v5/<int:id>/', SnippetDetailUpdateDeleteGenericApiView.as_view(), name="snippet-delete-v5"),
    
    path("user-snippet-list/v1/", UserSnippetlistApiView.as_view(), name="user-snippet-list-v1"),
    path("user-snippet-detail/v1/<uuid:user_id>/", UserSnippetDetailApiView.as_view(), name="user-snippet-detail-v1"),

]
urlpatterns = format_suffix_patterns(urlpatterns) 
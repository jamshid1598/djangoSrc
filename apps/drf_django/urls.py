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

    SnippetListCreateHyperlinkedApiView,
    UserSnippetListHyperlinkedApiView,
)

app_name='drf'

# router = routers.DefaultRouter()
# router.register(r"snippet", snippet_list)

urlpatterns = [
    # path('', include(router.urls)),

    path("", api_root, name="api-root"),
    path("snippet/<int:id>/highlighted/", SnippetHighlighted.as_view(), name="snippet-highlighted"),

    path("snippet-list-create/v1/", snippet_list_create_v1, name='snippet-list-create-v1'),
    path("snippet-detail-update-delete/v1/<int:id>/", snippet_detail_v1, name="snippet-detail-update-delete-v1"),
    
    path('snippet-list-create/v2/', snippet_list_create_v2, name='snippet-list-create-v2'),
    path("snippet-detail/v2/<int:id>/", snippet_detail_v2, name="snippet-detail-v2"),

    path("snippet-update/v2/<int:id>/", snippet_detail_v2, name="snippet-update-v2"),
    path("snippet-delete/v2/<int:id>/", snippet_detail_v2, name="snippet-delete-v2"),
    
    path('snippet-list-create/v3/', SnippetListCreateAPIView.as_view(), name="snippet-list-create-v3"),
    path("snippet-create-update-delete/v3/<int:id>/", 
         SnippetDetailUpdateDeleteAPIView.as_view(), 
         name="snippet-detail-update-delete-v3"),
    
    path('snippet-list-create/v4/', SnippetListCreateMixinView.as_view(), name="snippet-list-create-v4"),
    path('snippet-detail-update-delete/v4/<int:id>/', 
         SnippetDetailUpdateDeleteMixinView.as_view(), 
         name="snippet-detail-update-delete-v4"),
    
    path('snippet-list-create/v5/', SnippetListCreateGenericApiView.as_view(), name="snippet-list-create-v5"),
    path('snippet-detail-update-delete/v5/<int:id>/', 
         SnippetDetailUpdateDeleteGenericApiView.as_view(), 
         name="snippet-detail-update-delete-v5"),
    
    path("snippet-list-create/v6/", SnippetListCreateHyperlinkedApiView.as_view(), name='snippet-list-create-v6'),
    
    path("user-snippet-list/v1/", 
         UserSnippetlistApiView.as_view(), name="user-snippet-list-v1"),
    path("user-snippet-detail/v1/<uuid:user_id>/", 
         UserSnippetDetailApiView.as_view(), name="user-snippet-detail-v1"),

    path("user-snippet-list/v2/", 
         UserSnippetListHyperlinkedApiView.as_view(), name="user-snippet-list-v2"),
]
urlpatterns = format_suffix_patterns(urlpatterns) 
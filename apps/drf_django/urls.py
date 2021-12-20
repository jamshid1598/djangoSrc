from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    # function based views
    snippet_list_v1,
    snippet_list_v2,
    snippet_detail_v1,
    snippet_detail_v2,

    # APIView class based views
    SnippetListAPIView,
    SnippetDetailAPIView,
    
    # Mixins class based views
    SnippetListMixinView,
    SnippetDetailMixinView,
    
    # Generic class based views
    SnippetListGenericView,
    SnippetDetailGenericView,
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
    
    path("snippet-list/v3/", SnippetListAPIView.as_view(), name='snippet-list-v3'),
    path("snippet-detail/v3/<int:id>/", SnippetDetailAPIView.as_view(), name='snippet-detail-v3'),
    
    path("snippet-list/v4/", SnippetListMixinView.as_view(), name='snippet-list-v4'),
    path("snippet-detail/v4/<int:id>/", SnippetDetailMixinView.as_view(), name='snippet-detail-v4'),
    
    path("snippet-list/v5/", SnippetListGenericView.as_view(), name='snippet-list-v5'),
    path("snippet-detail/v5/<int:id>/", SnippetDetailGenericView.as_view(), name='snippet-detail-v5'),
]
urlpatterns = format_suffix_patterns(urlpatterns) 
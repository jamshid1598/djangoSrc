"""projectroot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('jet/', include('jet.urls', namespace='jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
    path('api-auth/v1/', include("rest_framework.urls", namespace='rest_framework')),
    # path('api-auth/', include('rest_framework.urls')),
    
    path("",         include("apps.core.urls", namespace='core')),
    path("blog/",    include("apps.blog.urls", namespace="blog")),
    path("account/", include("apps.users.urls", namespace='users')),
    path("drf/",     include("apps.drf_docs.urls", namespace='drf')),
    path("signals/", include("apps.signals_django.urls", namespace='signals')),
    path('import_export/', include("apps.django_import_export.urls", namespace='django_export_import')),
    path('import/', include("apps.studentExam.urls", namespace='import')),
    path("try-drf/", include("apps.tryDrf.urls", namespace="try-drf")),
    path("jet-reboot/", include("apps.jetReboot.urls", namespace="jet_reboot")),
    path("htmx/", include("apps.htmx.urls", namespace="htmx")),
    # path('celery/',  include("apps.django_celery.urls", namespace='django-celery')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
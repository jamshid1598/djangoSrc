from django.urls import path 
from .views import SendFeedbackView

app_name='django-celery'

urlpatters = [
    path('feedback/', SendFeedbackView.as_view(), name='send-feedback'),
]
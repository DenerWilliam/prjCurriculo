from django.urls import path
from .views import PersonalDataAPIView

urlpatterns = [
    path('personal/', PersonalDataAPIView.as_view(), name='personal-data-api'),
]
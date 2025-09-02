from django.urls import path
from .views import (
    ProfessionalExperienceListCreateView,
    ProfessionalExperienceRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', ProfessionalExperienceListCreateView.as_view(), name='experience-list-create'),
    path('<int:pk>/', ProfessionalExperienceRetrieveUpdateDestroyView.as_view(), name='experience-detail'),
]

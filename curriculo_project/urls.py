from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as URLs da app personal_data
    path('api/v1/curriculo/personal/', include('personal_data.urls')),
    path('api/v1/curriculo/experiences/', include('professional_experience.urls')),
]

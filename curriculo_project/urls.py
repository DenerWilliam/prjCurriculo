from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as URLs da app personal_data
    path('api/v1/curriculo/', include('personal_data.urls')),
]

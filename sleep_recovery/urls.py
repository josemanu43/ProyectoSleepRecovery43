"""
URL configuration for sleep_recovery project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de Administración
    path('admin/', admin.site.urls),

    # Rutas de Google Login (allauth)
    path('accounts/', include('allauth.urls')),

    # Rutas de la aplicación 'users' (Aquí vive 'index')
    # IMPORTANTE: Esta línea conecta tu proyecto con tu app.
    path('', include('users.urls')), 
]
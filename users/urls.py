# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL para la página principal (dashboard) después del login
    path('', views.dashboard, name='dashboard'),
    
    # URL para el registro de usuarios
    path('register/', views.register, name='register'),
    
    # URL para el inicio de sesión de usuarios
    path('login/', views.user_login, name='login'),
    
    # URL para cerrar la sesión
    path('logout/', views.user_logout, name='logout'),
]
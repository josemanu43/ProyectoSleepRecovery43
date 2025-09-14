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

    path('add_sleep_session/', views.add_sleep_session, name='add_sleep_session'),
]

# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-sleep-session/', views.add_sleep_session, name='add_sleep_session'),
    path('edit-sleep-session/<int:session_id>/', views.edit_sleep_session, name='edit_sleep_session'), # Nueva URL para editar
    path('delete-sleep-session/<int:session_id>/', views.delete_sleep_session, name='delete_sleep_session'), # Nueva URL para eliminar
]
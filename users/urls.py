from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ============================
    # 1. PÁGINA DE INICIO (LANDING PAGE)
    # ============================
    path('', views.index, name='index'),

    # ============================
    # 2. AUTENTICACIÓN Y USUARIOS
    # ============================
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # ============================
    # 3. DASHBOARD Y GESTIÓN DE SUEÑO
    # ============================
    # Panel Principal
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Historial (Tabla completa)
    path('history/', views.sleep_history, name='sleep_history'),

    # CRUD (Crear, Editar, Eliminar)
    path('dashboard/add/', views.add_sleep_session, name='add_sleep_session'),
    path('dashboard/edit/<int:session_id>/', views.edit_sleep_session, name='edit_sleep_session'),
    path('dashboard/delete/<int:session_id>/', views.delete_sleep_session, name='delete_sleep_session'),

    # ============================
    # 4. RECUPERACIÓN DE CONTRASEÑA
    # ============================
    # Paso 1: Formulario para ingresar el correo
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name='password_reset'),

    # Paso 2: Mensaje de "Correo enviado"
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"),
         name='password_reset_done'),

    # Paso 3: Formulario para ingresar la nueva contraseña (link del correo)
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"),
         name='password_reset_confirm'),

    # Paso 4: Mensaje de éxito
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),

    path('terms/', views.terms, name='terms'),
]
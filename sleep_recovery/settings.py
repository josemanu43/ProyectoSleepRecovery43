"""
Django settings for sleep_recovery project.
"""
from pathlib import Path
import os
from decouple import config

# ----------------------------------------------------
# 1. CONFIGURACIÓN DE APIs Y CLAVES
# ----------------------------------------------------
# Nota: Para producción, asegúrate de que estas claves estén en un archivo .env
WEATHER_API_KEY = config("WEATHER_API_KEY", default="83e4e02b2b714137b76215104252709")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7xeo8+)(^l=@@wj6dc)86x5o-b*c6xql=zdwq#szvmob$hioea'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# ----------------------------------------------------
# 2. APLICACIONES INSTALADAS
# ----------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tus aplicaciones
    'users',
    
    # Requeridas por allauth (Login Social)
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1


# ----------------------------------------------------
# 3. AUTENTICACIÓN Y MIDDLEWARE
# ----------------------------------------------------

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend', # Requerido por allauth
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # Login estándar
    'allauth.account.auth_backends.AuthenticationBackend', # Login social y avanzado
]

SITE_ID = 1

# Permite login con username O email
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# Requiere el email en el registro (necesario para login por email)
ACCOUNT_EMAIL_REQUIRED = True
# No requiere un username único si se usa email (opcional, depende de tu gusto)
ACCOUNT_USERNAME_REQUIRED = False
# Para desarrollo, no verificamos el email (cambiar a 'mandatory' en producción)
ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # Middleware de allauth
]

# Configuración de redirecciones
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'


# ----------------------------------------------------
# 4. TEMPLATES Y RUTAS
# ----------------------------------------------------

ROOT_URLCONF = 'sleep_recovery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'users/templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sleep_recovery.wsgi.application'


# ----------------------------------------------------
# 5. CONFIGURACIÓN DE BASE DE DATOS (PostgreSQL)
# ----------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_sleep_recovery',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# ----------------------------------------------------
# 6. VALIDACIÓN DE CONTRASEÑAS
# ----------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ----------------------------------------------------
# 7. INTERNACIONALIZACIÓN (I18N)
# ----------------------------------------------------

LANGUAGE_CODE = 'es-co' 
TIME_ZONE = 'America/Bogota' 
USE_I18N = True
USE_TZ = True


# ----------------------------------------------------
# 8. ARCHIVOS ESTÁTICOS
# ----------------------------------------------------

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'users/static', 
]
STATIC_ROOT = BASE_DIR / 'staticfiles' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ----------------------------------------------------
# 9. CONFIGURACIÓN SOCIAL ACCOUNT
# ----------------------------------------------------

# NOTA IMPORTANTE:
# No definimos SOCIALACCOUNT_PROVIDERS aquí.
# La configuración de Google (Client ID y Secret) se lee 
# directamente desde la Base de Datos (Panel de Administración -> Aplicaciones Sociales).
# Esto previene errores de duplicidad y protege las claves en GitHub.

# Imprime los correos en la consola en lugar de enviarlos (SOLO DESARROLLO)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
import io
import base64
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Importaciones de tus módulos
from .forms import SleepSessionForm
from .models import SleepSession
from .recommendations.factories import AdviceFactory
from .api_fetcher import get_weather_info

# ============================
# PÁGINAS PÚBLICAS
# ============================

def index(request):
    """Renderiza la página de aterrizaje."""
    return render(request, 'users/index.html')

# ============================
# DASHBOARD PRINCIPAL
# ============================

@login_required
def dashboard(request):
    current_user = request.user
    
    # Obtener sesiones reales de la base de datos
    sleep_sessions = SleepSession.objects.filter(user=current_user).order_by('start_time')
    
    # Preparar datos para Pandas
    sessions_data = list(sleep_sessions.values(
        'start_time', 'end_time', 'duration', 'quality__quality_label', 'sleep_interruptions'
    ))

    chart_url = None
    advice = []
    average_duration = 0
    total_sessions = 0
    most_frequent_quality = "No hay datos"
    
    # Obtener clima real
    try:
        temp_celsius, condition = get_weather_info(city="Medellin")
    except Exception as e:
        print(f"Error clima: {e}")
        temp_celsius, condition = 24, "No disponible"

    if sessions_data:
        df = pd.DataFrame(sessions_data)
        df['start_time'] = pd.to_datetime(df['start_time'])

        # Generar gráfico
        plt.figure(figsize=(10, 5))
        plt.plot(df['start_time'], df['duration'], marker='o', linestyle='-', color='#0d6efd')
        plt.title('Duración del sueño')
        plt.xlabel('Fecha')
        plt.ylabel('Minutos')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        chart_url = base64.b64encode(buf.getvalue()).decode('utf8')
        buf.close()
        plt.close()

        #Estadísticas
        average_duration = df['duration'].mean()
        total_sessions = len(df)
        if not df['quality__quality_label'].mode().empty:
            most_frequent_quality = df['quality__quality_label'].mode()[0]

        # Consejos (Pattern Strategy)
        # 1. Duración
        advice.append(AdviceFactory.get_advice_generator('duration').get_advice(average_duration))
        
        # 2. Consistencia
        if total_sessions > 1:
            advice.append(AdviceFactory.get_advice_generator('consistency').get_advice(df))
        
        # 3. Consejo de Clima (CORREGIDO / NORMALIZADO)
        # Obtenemos el consejo original (que usa 'category' y 'message')
        temp_advice_raw = AdviceFactory.get_advice_generator('temperature').get_advice(temp_celsius)
        
        # Creamos un nuevo diccionario con las claves estándar ('type' y 'text')
        # para evitar el error en el template
        temp_advice_clean = {
            'type': temp_advice_raw.get('category', 'Temperatura'),
            'text': temp_advice_raw.get('message', ''),
            'metric': temp_advice_raw.get('metric', '')
        }
        advice.append(temp_advice_clean)

    # Contexto para el template
    context = {
        'user': current_user,
        'sleep_sessions': sleep_sessions,
        'average_duration': average_duration,
        'total_sessions': total_sessions,
        'most_frequent_quality': most_frequent_quality,
        'chart_url': chart_url,
        'advice': advice,
        'current_temp': temp_celsius,
        'current_condition': condition,
        'target_duration_minutes': 480, 
        'sleep_quality_score': 0, 
        'sessions_last_7_days': sleep_sessions.count(), 
        'duration_delta_percentage': 0,
    }

    return render(request, 'users/dashboard.html', context)

# ============================
# HISTORIAL (NUEVA VISTA)
# ============================

@login_required
def sleep_history(request):
    """Muestra el historial completo de sesiones con opciones de editar/borrar."""
    sleep_sessions = SleepSession.objects.filter(user=request.user).order_by('-start_time')
    
    context = {
        'sleep_sessions': sleep_sessions
    }
    return render(request, 'users/sleep_history.html', context)

# ============================
# GESTIÓN DE SESIONES (CRUD)
# ============================

@login_required
def add_sleep_session(request):
    if request.method == 'POST':
        form = SleepSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            if session.end_time and session.start_time:
                diff = session.end_time - session.start_time
                session.duration = diff.total_seconds() / 60
            session.save()
            return redirect('dashboard')
    else:
        form = SleepSessionForm(initial={'start_time': timezone.now(), 'end_time': timezone.now()})
    return render(request, 'users/add_sleep_session.html', {'form': form})

@login_required
def edit_sleep_session(request, session_id):
    session = get_object_or_404(SleepSession, pk=session_id, user=request.user)
    if request.method == 'POST':
        form = SleepSessionForm(request.POST, instance=session)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.end_time and obj.start_time:
                diff = obj.end_time - obj.start_time
                obj.duration = diff.total_seconds() / 60
            obj.save()
            return redirect('sleep_history') 
    else:
        form = SleepSessionForm(instance=session)
    return render(request, 'users/edit_sleep_session.html', {'form': form, 'session': session})

@login_required
def delete_sleep_session(request, session_id):
    session = get_object_or_404(SleepSession, pk=session_id, user=request.user)
    if request.method == 'POST':
        session.delete()
        return redirect('sleep_history') 
    return render(request, 'users/delete_sleep_session.html', {'sleep_session': session})

# ============================
# AUTENTICACIÓN
# ============================

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

def terms(request):
    """Renderiza la página de términos y condiciones."""
    return render(request, 'users/terms.html')

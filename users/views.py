# users/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import SleepSessionForm, SleepSessionEditForm
from .models import SleepSession, SleepQualityOption
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

# Vista para la página principal (dashboard)
@login_required
def dashboard(request):
    sleep_sessions = SleepSession.objects.filter(user=request.user).order_by('start_time')
    sessions_data = list(sleep_sessions.values('start_time', 'end_time', 'duration', 'quality__quality_label'))

    chart_url = None
    average_duration = 0
    total_sessions = 0
    most_frequent_quality = "No hay datos"

    if sessions_data:
        df = pd.DataFrame(sessions_data)
        
        # Generar el gráfico de duración del sueño
        plt.figure(figsize=(10, 5))
        plt.plot(df['start_time'], df['duration'], marker='o')
        plt.title('Duración del sueño a lo largo del tiempo')
        plt.xlabel('Fecha')
        plt.ylabel('Duración (minutos)')
        plt.grid(True)
        
        # Convertir el gráfico a una imagen base64
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        chart_url = base64.b64encode(buf.getvalue()).decode('utf8')
        buf.close()
        
        # Calcular estadísticas
        average_duration = df['duration'].mean()
        total_sessions = len(df)
        
        # Encontrar la calidad de sueño más frecuente
        most_frequent_quality_series = df['quality__quality_label'].mode()
        if not most_frequent_quality_series.empty:
            most_frequent_quality = most_frequent_quality_series.iloc[0]

    context = {
        'sleep_sessions': sleep_sessions,
        'average_duration': average_duration,
        'total_sessions': total_sessions,
        'most_frequent_quality': most_frequent_quality,
        'chart_url': chart_url
    }
    
    return render(request, 'users/dashboard.html', context)

# Vista para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Vista para el inicio de sesión
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Vista para cerrar la sesión
def user_logout(request):
    logout(request)
    return redirect('login')

# Vista para agregar una sesión de sueño
@login_required
def add_sleep_session(request):
    if request.method == 'POST':
        form = SleepSessionForm(request.POST)
        if form.is_valid():
            sleep_session = SleepSession(
                user=request.user,
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
                quality=form.cleaned_data['quality'],
                sleep_interruptions=form.cleaned_data['sleep_interruptions']
            )
            sleep_session.duration = (sleep_session.end_time - sleep_session.start_time).total_seconds() / 60
            sleep_session.save()
            return redirect('dashboard')
    else:
        form = SleepSessionForm(initial={'start_time': timezone.now(), 'end_time': timezone.now()})
    return render(request, 'users/add_sleep_session.html', {'form': form})

# Vista para editar una sesión de sueño existente
@login_required
def edit_sleep_session(request, session_id):
    sleep_session = get_object_or_404(SleepSession, pk=session_id, user=request.user)
    if request.method == 'POST':
        form = SleepSessionEditForm(request.POST, instance=sleep_session) # Cambiado
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SleepSessionEditForm(instance=sleep_session) # Cambiado
    context = {'form': form}
    return render(request, 'users/edit_sleep_session.html', context)

# Vista para eliminar una sesión de sueño
@login_required
def delete_sleep_session(request, session_id):
    sleep_session = get_object_or_404(SleepSession, pk=session_id, user=request.user)
    if request.method == 'POST':
        sleep_session.delete()
        return redirect('dashboard')
    return render(request, 'users/delete_sleep_session.html', {'sleep_session': sleep_session})
from django import forms
from .models import SleepSession, SleepQualityOption

class SleepSessionForm(forms.Form):
    # Este formulario es para la creación de una nueva sesión
    start_time = forms.DateTimeField(
        label='Hora de inicio del sueño',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    end_time = forms.DateTimeField(
        label='Hora de fin del sueño',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    quality = forms.ModelChoiceField(
        queryset=SleepQualityOption.objects.all(),
        label='Calidad del sueño'
    )
    sleep_interruptions = forms.IntegerField(
        label='Interrupciones (número de veces que te despertaste)',
        required=False
    )

class SleepSessionEditForm(forms.ModelForm):
    # Este formulario es para la edición de una sesión existente
    class Meta:
        model = SleepSession
        fields = ['start_time', 'end_time', 'quality', 'sleep_interruptions']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
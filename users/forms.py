from django import forms
from django.utils import timezone
from .models import SleepSession, SleepQualityOption


class SleepSessionForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    end_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = SleepSession
        fields = ['start_time', 'end_time', 'quality', 'sleep_interruptions']

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_time')
        end = cleaned_data.get('end_time')

        if start and end:
            if end <= start:
                raise forms.ValidationError("La hora de fin debe ser posterior a la de inicio.")
            if end > timezone.now():
                raise forms.ValidationError("No puedes registrar horas futuras de sueño.")

        return cleaned_data


class SleepSessionEditForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    end_time = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = SleepSession
        fields = ['start_time', 'end_time', 'quality', 'sleep_interruptions']

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_time')
        end = cleaned_data.get('end_time')

        if start and end:
            if end <= start:
                raise forms.ValidationError("La hora de fin debe ser posterior a la de inicio.")
            if end > timezone.now():
                raise forms.ValidationError("No puedes registrar horas futuras de sueño.")

        return cleaned_data


class SleepSessionDeleteForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label="Confirma que deseas eliminar esta sesión"
    )

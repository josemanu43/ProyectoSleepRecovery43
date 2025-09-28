# users/recommendations/advice_logic.py
from abc import ABC, abstractmethod
import pandas as pd


class BaseAdvice(ABC):
    """Interfaz base para todos los tipos de consejos."""
    @abstractmethod
    def get_advice(self, data):
        pass

class DurationAdvice(BaseAdvice):
    """Consejos basados en la duración promedio del sueño."""
    def get_advice(self, average_duration):
        if average_duration < 360: # Menos de 6 horas (360 min)
            return {
                'type': 'Duración',
                'text': 'Tu duración promedio de sueño es baja. Intenta ir a la cama 30 minutos antes de lo habitual para mejorar tu descanso.',
                'metric': f'{average_duration:.0f} min'
            }
        elif average_duration > 540: # Más de 9 horas (540 min)
            return {
                'type': 'Duración',
                'text': 'Estás durmiendo demasiado tiempo. Esto puede indicar fatiga subyacente. Asegúrate de tener una rutina matutina consistente.',
                'metric': f'{average_duration:.0f} min'
            }
        else:
            return {
                'type': 'Duración',
                'text': '¡Excelente! Tu duración de sueño está dentro del rango recomendado (7-9 horas). Mantén esta consistencia.',
                'metric': f'{average_duration:.0f} min'
            }

class ConsistencyAdvice(BaseAdvice):
    """Consejos basados en la consistencia de las horas de sueño/vigilia."""
    def get_advice(self, sleep_sessions_df):
        # La consistencia se calcula midiendo la desviación estándar (STD) de las horas de inicio de sueño.
        # Cuanto menor sea el STD, más consistente es el horario.
        
        # Convertir 'start_time' a solo la hora del día (minutos desde medianoche)
        sleep_sessions_df['start_hour_min'] = (
            sleep_sessions_df['start_time'].dt.hour * 60 + 
            sleep_sessions_df['start_time'].dt.minute
        )
        
        # Calcular la desviación estándar en minutos
        std_minutes = sleep_sessions_df['start_hour_min'].std()
        
        if pd.isna(std_minutes) or std_minutes > 60: # Más de 1 hora de desviación
            return {
                'type': 'Consistencia',
                'text': 'Tu horario de sueño es muy inconsistente. Intenta acostarte y levantarte a la misma hora, incluso los fines de semana.',
                'metric': f'{std_minutes:.0f} min de desviación'
            }
        else:
            return {
                'type': 'Consistencia',
                'text': 'Tienes una buena consistencia en tus horarios de sueño. Esto es clave para regular tu ritmo circadiano.',
                'metric': f'{std_minutes:.0f} min de desviación'
            }
        
# advice_logic.py

class DurationAdviceGenerator:
    def get_advice(self, average_duration):
        # lógica de duración...
        return {"category": "Duración", "message": "...", "metric": f"{average_duration} min"}


class ConsistencyAdviceGenerator:
    def get_advice(self, df):
        # lógica de consistencia...
        return {"category": "Consistencia", "message": "...", "metric": f"{...} min de desviación"}


class TemperatureAdviceGenerator:
    def get_advice(self, temp_celsius):
        if temp_celsius is None:
            return {
                "category": "Temperatura",
                "message": "No se pudo obtener la temperatura actual.",
                "metric": "N/A"
            }

        if temp_celsius < 18:
            message = "La temperatura está algo fría. Usa una cobija extra o asegúrate de mantener la habitación cálida."
        elif 18 <= temp_celsius <= 24:
            message = "La temperatura es agradable para dormir. Mantén la ventilación adecuada."
        else:
            message = "Hace calor. Considera ventilar la habitación o usar ropa ligera para dormir mejor."

        return {
            "category": "Temperatura",
            "message": message,
            "metric": f"{temp_celsius}°C"
        }


class AdviceFactory:
    generators = {
        "duration": DurationAdviceGenerator(),
        "consistency": ConsistencyAdviceGenerator(),
        "temperature": TemperatureAdviceGenerator(),  # 👈 aquí agregas el tuyo
    }

    @staticmethod
    def get_advice_generator(advice_type):
        return AdviceFactory.generators.get(advice_type)

class TemperatureAdvice:
    def get_advice(self, temp_celsius):
        if temp_celsius is None:
            return {
                "category": "Temperatura",
                "message": "No se pudo obtener la temperatura actual.",
                "metric": "N/A"
            }

        if temp_celsius < 18:
            message = "Tu habitación está demasiado fría, intenta subir la calefacción."
        elif temp_celsius > 24:
            message = "Tu habitación está demasiado caliente, intenta ventilarla o usar aire acondicionado."
        else:
            message = "La temperatura de tu habitación es adecuada para dormir."

        return {
            "category": "Temperatura",
            "message": message,
            "metric": f"{temp_celsius}°C"
        }

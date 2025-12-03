# users/templatetags/sleep_filters.py
from django import template

register = template.Library()

@register.filter(name='minutes_to_hours')
def minutes_to_hours(value):
    """
    Convierte un valor en minutos a un formato legible de horas y minutos (ej. 7h 30m).
    Maneja valores nulos o no numéricos devolviendo '0m'.
    """
    if value is None:
        return "0m"
    try:
        minutes = int(value)
    except (ValueError, TypeError):
        return "0m" # O podrías devolver el valor original: return value

    hours = minutes // 60
    remaining_minutes = minutes % 60

    if hours > 0:
        return f"{hours}h {remaining_minutes}m"
    else:
        return f"{remaining_minutes}m"
# users/recommendations/factories.py
from .advice_logic import DurationAdvice, ConsistencyAdvice

class AdviceFactory:
    """Fábrica que crea la instancia de un consejo basado en el tipo."""
    
    @staticmethod
    def get_advice_generator(advice_type):
        if advice_type == 'duration':
            return DurationAdvice()
        elif advice_type == 'consistency':
            return ConsistencyAdvice()
        else:
            raise ValueError(f"Tipo de consejo no soportado: {advice_type}")
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_migrate

# ====================================================================
# MODELO 1: Perfil de Usuario (RESTUARADO)
# ====================================================================
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True, verbose_name="Edad")
    gender = models.CharField(max_length=50, null=True, blank=True, verbose_name="Género")
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Peso (kg)")
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Altura (m)")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

# ====================================================================
# MODELO 2: Opciones de Calidad del Sueño (Mejora de tu compañera)
# ====================================================================
class SleepQualityOption(models.Model):
    """Define las opciones predefinidas para calificar la calidad del sueño."""
    
    quality_label = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Etiqueta de Calidad"
    )
    
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], 
        verbose_name="Puntuación (1-5)",
        help_text="Puntuación numérica de la calidad (1 es muy mala, 5 es excelente)."
    )

    class Meta:
        verbose_name = "Opción de Calidad de Sueño"
        verbose_name_plural = "Opciones de Calidad de Sueño"
        ordering = ['-score']

    def __str__(self):
        return f"{self.quality_label} ({self.score})"

# ====================================================================
# MODELO 3: Sesión de Sueño (Mejora de tu compañera + Tus datos)
# ====================================================================
class SleepSession(models.Model):
    """Almacena la información de una sesión de sueño registrada por el usuario."""
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sleep_sessions',
        verbose_name="Usuario"
    )
    
    start_time = models.DateTimeField(verbose_name="Hora de Inicio")
    end_time = models.DateTimeField(verbose_name="Hora de Fin")
    
    duration = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Duración (minutos)",
        help_text="Calculado a partir de la diferencia entre Inicio y Fin."
    )
    
    quality = models.ForeignKey(
        SleepQualityOption,
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name="Calidad del Sueño"
    )
    
    sleep_interruptions = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Interrupciones"
    )
    
    # Campo JSON para datos avanzados (RESTUARADO de tu versión)
    sleep_stage_data = models.JSONField(null=True, blank=True, verbose_name="Datos de Fases (JSON)")
    
    notes = models.TextField(blank=True, verbose_name="Notas Adicionales")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sesión de Sueño"
        verbose_name_plural = "Sesiones de Sueño"
        ordering = ['-start_time']

    def __str__(self):
        duration_str = f"{self.duration // 60}h {self.duration % 60}m" if self.duration else "N/A"
        return f"Sesión de {self.user.username} - {self.start_time.strftime('%Y-%m-%d')} ({duration_str})"

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            time_difference = self.end_time - self.start_time
            self.duration = int(time_difference.total_seconds() / 60)
        super().save(*args, **kwargs)

# ====================================================================
# MODELO 4: Recomendaciones (RESTUARADO)
# ====================================================================
class Recommendation(models.Model):
    RECOMMENDATION_TYPES = [
        ('consistencia', 'Consistencia'),
        ('ambiente', 'Ambiente'),
        ('duracion', 'Duración'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField()
    recommendation_type = models.CharField(max_length=50, choices=RECOMMENDATION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    read_by_user = models.BooleanField(default=False)

    def __str__(self):
        return f'Recomendación para {self.user.username}'

# ====================================================================
# CONFIGURACIÓN INICIAL (Creación de opciones por defecto)
# ====================================================================
def create_default_quality_options(sender, **kwargs):
    if kwargs.get('created', False):
        return

    options = [
        ("Excelente", 5),
        ("Muy Buena", 4),
        ("Normal", 3),
        ("Mala", 2),
        ("Muy Mala", 1),
    ]

    for label, score in options:
        SleepQualityOption.objects.get_or_create(
            quality_label=label,
            defaults={'score': score}
        )
        
post_migrate.connect(create_default_quality_options, sender=SleepSession._meta.app_config)

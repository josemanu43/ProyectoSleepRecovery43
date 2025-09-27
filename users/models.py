from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Profile for {self.user.username}'

from django.db import models
from django.contrib.auth.models import User

class SleepQualityOption(models.Model):
    quality_label = models.CharField(max_length=50)

    def __str__(self):
        return self.quality_label

class SleepSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField()  # Duración en minutos
    quality = models.ForeignKey(SleepQualityOption, on_delete=models.SET_NULL, null=True)
    sleep_interruptions = models.IntegerField(default=0, null=True, blank=True)
    sleep_stage_data = models.JSONField(null=True, blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Sleep session for {self.user.username} on {self.start_time.date()}'

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
        return f'Recommendation for {self.user.username}'

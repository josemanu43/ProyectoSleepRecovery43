# users/admin.py
from django.contrib import admin
from .models import UserProfile, SleepSession, SleepQualityOption, Recommendation

# Registrar los modelos para que aparezcan en el panel de administración
admin.site.register(UserProfile)
admin.site.register(SleepSession)
admin.site.register(SleepQualityOption)
admin.site.register(Recommendation)
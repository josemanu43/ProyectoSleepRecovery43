# users/admin.py

from django.contrib import admin
from .models import UserProfile, SleepSession, SleepQualityOption, Recommendation

# 1. Personalización del texto del panel de administración (Requisito de presentación)
admin.site.site_header = "Administración de Sleep Recovery"
admin.site.site_title = "Panel de Control SR"
admin.site.index_title = "Bienvenido al Panel de Sleep Recovery"

# 2. Registra todos los modelos una sola vez para evitar el error AlreadyRegistered
admin.site.register(UserProfile)
admin.site.register(SleepSession)
admin.site.register(SleepQualityOption)
admin.site.register(Recommendation)

# 3. Nota sobre la inyección de CSS:
# El código para inyectar CSS a través de una clase CustomAdmin NO es la forma estándar de Django.
# Para cambiar el color, es más limpio usar el sistema de archivos estáticos (collectstatic).
# Por ahora, dejamos el archivo limpio y funcional.
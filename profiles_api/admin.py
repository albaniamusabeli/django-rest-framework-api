from django.contrib import admin
from profiles_api import models

# Registrar el modelo creado en models.py para usarlo en el panel administrador de Django
admin.site.register(models.UserProfile)
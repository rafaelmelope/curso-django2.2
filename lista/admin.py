from django.contrib import admin

from .models import Lista  # 1 - Importar Models Lista

admin.site.register(Lista) # 2 - Registrar Models Lista para aparecer no Admin.

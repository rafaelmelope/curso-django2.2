from django.contrib import admin
from .models import Post  # 1 - adicionar models Post para aparecer no Admin.

admin.site.register(Post) # 2 - adicionar models Post para aparecer no Admin.

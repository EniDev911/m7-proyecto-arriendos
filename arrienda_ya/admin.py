from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from django.contrib.auth.models import User
# Register your models here.

class UsuarioInline(admin.TabularInline):
  model = Usuario
  can_delete = False
  verbose_name_plural = "Usuario"

class CustomUsuarioAdmin(UserAdmin):
  inlines = (UsuarioInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUsuarioAdmin)

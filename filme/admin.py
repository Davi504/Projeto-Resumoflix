from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Filme, Episodio, Usuario

# A função 'append' deve adicionar uma tupla, não um dicionário
campos = list(UserAdmin.fieldsets)
campos.append(('Historico', {'fields': ('filmes_vistos',)}))
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)

from django.contrib import admin
from .models import Filme
from .models import Episodio

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
from django.contrib import admin
from .models import Cliente, Profesor, TipoEntrenamiento, Turno

admin.site.register(Cliente)
admin.site.register(Profesor)
admin.site.register(TipoEntrenamiento)
admin.site.register(Turno)


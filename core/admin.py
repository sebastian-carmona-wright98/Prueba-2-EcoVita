from django.contrib import admin
from .models import DatosPersona

# Register your models here.

class EcovitaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Direccion', 'Telefono', 'Mail')
    search_fields = ['Nombre']

admin.site.register(DatosPersona,EcovitaAdmin)




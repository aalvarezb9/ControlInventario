from django.contrib import admin

from .models import *

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'primer_nombre',
        'segundo_nombre',
        'primer_apellido',
        'segundo_apellido',
        'numero_de_identidad',
        'edad',
        'direccion',
        'salario',
        'sexo',
        'rol'
    )
    search_fields = ("numero_de_identidad",)
    readonly_fields = ('created',)
    list_per_page = 10

admin.site.register(Empleado, EmpleadoAdmin)
# admin.site.register(Sexo)
admin.site.register(Rol)

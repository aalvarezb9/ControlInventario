from django.contrib import admin

from .models import Venta, Concepto

# Register your models here.

class ConceptoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cantidad')
    list_per_page = 10

class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'empleado', 'total')
    list_filter = ('fecha', 'empleado')
    ordering = ('-fecha',)
    list_per_page = 10

admin.site.register(Concepto, ConceptoAdmin)
admin.site.register(Venta, VentaAdmin)
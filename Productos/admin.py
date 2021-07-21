from django.contrib import admin

# Register your models here.

from .models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'cantidad', 'disponible', 'imagen')
    search_fields = ('nombre',)
    list_filter = ('categoria',)
    readonly_fields = ('created', 'updated')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
    readonly_fields = ('created', 'updated')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
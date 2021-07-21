from django.db import models
from Empleados import models as emp_models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return f"{self.categoria}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    disponible = models.BooleanField()
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return f"{self.nombre} (L.{self.precio})"
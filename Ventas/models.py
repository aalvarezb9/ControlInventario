from django.db import models
from Productos import models as prd_models
from Empleados import models as emp_models
from datetime import datetime
# Create your models here.

class Venta(models.Model):
    empleado = models.ForeignKey(emp_models.Empleado, on_delete=models.RESTRICT)
    fecha = models.DateTimeField(default=datetime.now())
    total = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'

    def __str__(self):
        return f"{self.empleado} | {datetime.now()}"

class Concepto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.RESTRICT)
    producto = models.ForeignKey(prd_models.Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField()
    
    # def __init__(self, *args, **kwargs):
    #     self.actVentas(*args, **kwargs)

    # def actVentas(self, *args, **kwargs):
    #     producto = prd_models.Producto.objects.get(id=self.producto)
    #     venta = Venta.objects.get(id=self.venta)
    #     if venta.total is None:
    #         venta.total = 0
    #     venta.total += self.cantidad * producto.precio
    #     venta.save()

    #     return super(Concepto, self).save(*args, **kwargs)
        

    class Meta:
        verbose_name = 'concepto'
        verbose_name_plural = 'conceptos'

    def __str__(self):
        return f"{self.producto} ({self.cantidad})"




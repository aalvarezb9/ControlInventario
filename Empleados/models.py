from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sexo(models.Model):
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.sexo

class Rol(models.Model):
    rol = models.CharField(max_length=20)

    def __str__(self):
        return self.rol

class Empleado(models.Model):
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    numero_de_identidad = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    salario = models.FloatField()
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    # ASIGNAR A UNA SUCURSAL: pendiente
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} | {self.numero_de_identidad}"



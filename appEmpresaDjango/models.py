from django.db import models


# Create your models here.
# Departamento 1-n Empleado n-m Habilidad
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidad = models.ManyToManyField(Habilidad)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Estar seguro del on_delete cascade

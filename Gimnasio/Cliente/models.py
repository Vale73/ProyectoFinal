from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    cliente = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.CharField(max_length=50)

    def __str__(self):
        return f"Turno de {self.cliente} el {self.fecha} a las {self.hora}"

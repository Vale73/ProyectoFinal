from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,default=None, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.usuario.username

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class TipoEntrenamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    entrenamiento = models.ForeignKey(TipoEntrenamiento, on_delete=models.CASCADE, default=None, null=True)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'{self.usuario} - {self.entrenamiento} - {self.fecha} {self.hora}'


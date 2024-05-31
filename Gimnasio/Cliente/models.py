from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,default=None, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def _str_(self):
        return self.usuario.username

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=200)
    descripcion = models.TextField()

    def _str_(self):
        return self.nombre

class TipoEntrenamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def _str_(self):
        return self.nombre

class Turno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    entrenamiento = models.ForeignKey(TipoEntrenamiento, on_delete=models.CASCADE, default=None, null=True)
    fecha = models.DateField()
    hora = models.TimeField()

    def _str_(self):
        return f'{self.usuario} - {self.entrenamiento} - {self.fecha} {self.hora}'

class ReservaTurno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.usuario} - {self.fecha} {self.hora}"

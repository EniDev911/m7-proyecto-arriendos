from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
  rut = models.CharField(max_length=9, unique=True)
  direccion = models.CharField(max_length=100)
  telefono = models.CharField(max_length=12, null=False)

class TipoUsuario(models.Model):
  TIPO_CHOICES = [('A', 'arrendatario'), ('B', 'arrendador')]
  tipo = models.CharField(max_length=1,choices=TIPO_CHOICES, default='A')

class Inmueble(models.Model):
  TIPO_INMUEBLE = [('A', 'terreno'), ('B', 'edificio'), ('C', 'casa')]
  id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
  tipo_inmueble = models.CharField(max_length=60, choices=TIPO_INMUEBLE)
  nombre_inmueble = models.CharField(max_length=100, null=False)
  descripcion = models.TextField()
  m2_construido = models.FloatField()
  numero_banos = models.IntegerField(default=0)
  numero_habitaciones = models.IntegerField(default=0)
  direccion = models.CharField(max_length=100)

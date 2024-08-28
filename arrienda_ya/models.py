from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return f"Se creo al usuario: {self.username}"
  
class TipoUsuario(models.Model):
  TIPO_USUARIO = [('a', 'arrendatario'), ('b', 'arrendador')]
  tipo = models.CharField(max_length=1,choices=TIPO_USUARIO, default='A')

  def __str__(self) -> str:
    return f"{self.get_tipo_display()}"

class Inmueble(models.Model):
  id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
  id_comuna = models.ForeignKey("Comuna", on_delete=models.CASCADE, null=True)
  id_region = models.ForeignKey("Region", on_delete=models.CASCADE, null=True)
  id_tipo_inmueble = models.ForeignKey("TipoInmueble", on_delete=models.CASCADE, null=True)
  nombre_inmueble = models.CharField(max_length=100, null=False)
  descripcion = models.TextField()
  m2_construido = models.FloatField()
  numero_banos = models.IntegerField(default=0)
  numero_habitaciones = models.IntegerField(default=0)
  direccion = models.CharField(max_length=100)
  m2_terreno = models.FloatField(default=0)
  numero_est = models.IntegerField(default=0)

class TipoInmueble(models.Model):
  tipo_inmueble = models.CharField(150)

class Comuna(models.Model):
  comuna = models.CharField(max_length=150)
  
class Region(models.Model):
  region = models.CharField(max_length=150)
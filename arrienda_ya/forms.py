from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comuna, Region

class UserForm(UserCreationForm):
  email = forms.EmailField(label="Correo electrónico")

  password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirme Contraseña', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    labels = {'username': ('Nombre de Usuario')}

class TipoForm(forms.Form):
  tipos = ((1, 'arrendatario'), (2, 'arrendador'))
  tipo = forms.ChoiceField(choices=tipos)
  rut = forms.CharField(label="rut", max_length=100)
  direccion = forms.CharField(label="direccion", max_length=100)
  telefono = forms.CharField(label="teléfono", max_length=100)

class NewInmuebleForm(forms.Form):
  comunas = [(x.id, x.comuna) for x in Comuna.objects.filter()]
  regiones = [(x.id, x.region) for x in Region.objects.filter()]
  nombre_comuna = lambda x: x[1]
  id_region = forms.ChoiceField(label="Región", choices=regiones)
  id_comuna = forms.ChoiceField(label="Comuna", choices=sorted(comunas, key=nombre_comuna))
  id_tipo_inmueble = forms.ChoiceField(label="Tipo de inmueble", choices="")
  nombre_inmueble = forms.CharField(label="Nombre Inmueble", max_length=100)
  descripcion = forms.CharField(label="Descripción del Inmueble", max_length=100)
  m2_construido = forms.CharField(label="M2 construidos", max_length=100)
  numero_banos = forms.CharField(label="N° de baños", max_length=100)
  numero_habitaciones = forms.CharField(label="N° de habitaciones")
  direccion = forms.CharField(label="dirección", max_length=100)
  m2_terreno = forms.CharField(label="M2 terreno", max_length=100)
  numero_est = forms.CharField(label="N° estacionamiento", max_length=100)

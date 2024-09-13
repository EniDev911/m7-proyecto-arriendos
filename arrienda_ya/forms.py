from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
  email = forms.EmailField(label="Correo electrónico")

  password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirme Contraseña', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    labels = {'username': ('Nombre de Usuario')}

class TipoForm(forms.Form):
  tipos = ((1, 'Arrendatario'), (2, 'Arrendador'))
  tipo = forms.ChoiceField(choices=tipos)
  rut = forms.CharField(label="rut", max_length=100)
  direccion = forms.CharField(label="direccion", max_length=100)
  telefono = forms.CharField(label="teléfono", max_length=100)
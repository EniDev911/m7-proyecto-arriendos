from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import TipoUsuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TipoForm, UserForm

# Create your views here.
def registerView(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/register_tipo?user='+str(form.cleaned_data['username']))
  else:
    form = UserForm()
  return render(request, 'registration/register.html', {'form': form})

def register_tipo_view(request):
  username = request.GET['user']
  if request.method == 'POST':
    form = TipoForm(request.POST)
    if form.is_valid():
      form = TipoForm(request.POST)
      print(form)
      tipo = form.cleaned_data['tipo']
      rut = form.cleaned_data['rut']
      direccion = form.cleaned_data['direccion']
      telefono = form.cleaned_data['telefono']
      user = User.objects.filter(username=username)[0]
      tipo_user = TipoUsuario.objects.filter(id=int(tipo))[0]
      # datos = Profile(user=user, id_tipo_user=tipo_user, rut=rut, direccion=direccion, telefono=telefono)
      # datos.save()
      return HttpResponseRedirect('/login/')

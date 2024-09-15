from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile, TipoUsuario, Usuario
from .forms import TipoForm, UserForm
from django.contrib.auth.models import User
# Create your views here.

def index_view(request):
  return render(request, 'index.html')

def register_view(request):
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
  if request.method == "POST":
    form = TipoForm(request.POST)
    if form.is_valid():
      tipo = form.cleaned_data['tipo']
      rut = form.cleaned_data['rut']
      direccion = form.cleaned_data['direccion']
      telefono = form.cleaned_data['telefono']
      user = User.objects.filter(username=username)[0]
      tipo_user = TipoUsuario.objects.filter(id=int(tipo))[0]
      profile_user = Profile(user=user,
                             id_tipo_user=tipo_user,
                             rut=rut,
                             direccion=direccion,
                             telefono=telefono
                             )
      profile_user.save()
      return redirect('login_url')
  else:
    form = TipoForm()
  return render(request, 'registration/register_tipo.html', {'form': form})

@login_required
def dashboard_view(request):
  return render(request, 'dashboard.html')
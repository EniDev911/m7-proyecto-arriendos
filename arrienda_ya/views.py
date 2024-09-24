from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comuna, Profile, Region, TipoUsuario, Usuario, Inmueble, TipoInmueble
from .forms import TipoForm, UserForm, NewInmuebleForm, UpdateInmuebleForm, UserUpdateForm
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

@login_required
def new_inmueble_view(request: HttpRequest):
  if request.method == 'POST' and request.user.profile.id_tipo_user_id == 2:
    form = NewInmuebleForm(request.POST)
    if form.is_valid():
      nuevo_inmueble = Inmueble(
        id_tipo_inmueble = TipoInmueble.objects.get(id=int(form.cleaned_data['id_tipo_inmueble'])),
        id_comuna = Comuna.objects.get(id=int(form.cleaned_data['id_comuna'])),
        id_region = Region.objects.get(id=int(form.cleaned_data['id_region'])),
        nombre_inmueble = form.cleaned_data['nombre_inmueble'],
        descripcion = form.cleaned_data['descripcion'],
        m2_construido = form.cleaned_data['m2_construido'],
        numero_banos = form.cleaned_data['numero_banos'],
        numero_habitaciones = form.cleaned_data['numero_habitaciones'],
        direccion = form.cleaned_data['direccion'],
        m2_terreno = form.cleaned_data['m2_terreno'],
        numero_est = form.cleaned_data['numero_est']
      )
      nuevo_inmueble.id_usuario_id = request.user.id
      nuevo_inmueble.save()
      return redirect('dashboard')
  else:
    form = NewInmuebleForm()
  return render(request, 'new_inmueble.html', {'form':form})

@login_required
def update_inmueble_view(request: HttpRequest, pk:int):
  inmueble = get_object_or_404(Inmueble, id=pk, id_usuario=request.user.id)
  if request.method == "POST":
    form = UpdateInmuebleForm(request.POST, instance=inmueble)
    if form.is_valid():
      form.save()
      return redirect('dashboard')
  else:
    form = UpdateInmuebleForm(instance=inmueble) 
  return render(request, 'edit_inmueble.html', {'form': form})

@login_required
def inmuebles_view(request: HttpRequest):
  inmuebles = Inmueble.objects.all()
  return render(request, 'inmuebles.html', {'inmuebles': inmuebles })

@login_required
def profile_view(request: HttpRequest):
  if request.method == "POST":
    form = UserUpdateForm(request.POST, instance=request.user)

    if form.is_valid():
      form.save()
      return redirect('dashboard')
  else:
    form = UserUpdateForm(instance=request.user)
  return render(request, 'registration/update_profile.html', {'form': form})

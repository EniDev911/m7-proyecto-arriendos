from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
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

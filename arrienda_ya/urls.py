from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('', views.index_view, name='home_url'),
  path('accounts/login/', LoginView.as_view(next_page='dashboard'), name='login_url'),
  path('logout/', LogoutView.as_view(next_page='home_url'), name='logout_url'),
  path('register/', views.register_view, name='register_url'),
  path('register_tipo/', views.register_tipo_view, name='register_tipo_url'),
  path('dashboard/', views.dashboard_view, name='dashboard'),
  path('new_inmueble/', views.new_inmueble_view, name='new_inmueble_url'),
  path('inmueble/update/<int:pk>', views.update_inmueble_view, name='update_inmueble_url'),
  path('inmuebles/', views.inmuebles_view, name='inmuebles_url'),
  path('update_profile/', views.profile_view, name='update_profile_url')
]
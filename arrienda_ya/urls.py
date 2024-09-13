from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('', views.index_view, name='home_url'),
  path('login/', LoginView.as_view(next_page='dashboard'), name='login_url'),
  path('logout/', LogoutView.as_view(next_page='home_url'), name='logout_url'),
  path('register/', views.register_view, name='register_url'),
  path('register_tipo/', views.register_tipo_view, name='register_tipo_url')
]


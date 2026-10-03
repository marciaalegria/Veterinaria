

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from mascotas import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),

    # Rutas de las mascotas
    path('', include('mascotas.urls')),

    # Inicio y cierre de sesión
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='mascotas/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]


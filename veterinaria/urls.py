
from django.contrib import admin
from django.urls import path, include
from mascotas import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('', include('mascotas.urls')),
]

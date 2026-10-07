
from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_mascota, name='registrar_mascota'),
    path('mascotas/', views.listar_mascotas, name='listar_mascotas'),
    path('editar/<int:id>/', views.editar_mascota, name='editar_mascota'),
    path('eliminar/<int:id>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('api/mascotas/', views.api_mascotas, name='api_mascotas'),
    path('api/mascotas/<int:id>/', views.api_mascota_detalle, name='api_mascota_detalle'),
]

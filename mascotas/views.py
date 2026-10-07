
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MascotaForm
from .models import Mascota
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import MascotaSerializer
from rest_framework.permissions import IsAuthenticated


@login_required
def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_mascota')
    else:
        form = MascotaForm()

    return render(request, 'mascotas/registrar.html', {'form': form})


@login_required
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/listar.html', {
        'mascotas': mascotas
    })


def inicio(request):
    return render(request, 'mascotas/inicio.html')


@login_required
def editar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)

    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm(instance=mascota)

    return render(request, 'mascotas/editar.html', {
        'form': form,
        'mascota': mascota
    })


@login_required
def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)

    if request.method == 'POST':
        mascota.delete()
        return redirect('listar_mascotas')

    return render(request, 'mascotas/eliminar.html', {
        'mascota': mascota
    })
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_mascotas(request):

    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MascotaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])

def api_mascota_detalle(request, id):
    try:
        mascota = Mascota.objects.get(id=id)
    except Mascota.DoesNotExist:
        return Response(
            {'error': 'Mascota no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MascotaSerializer(
            mascota,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        mascota.delete()
        return Response(
            {'mensaje': 'Mascota eliminada correctamente'},
            status=status.HTTP_204_NO_CONTENT
        )

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MascotaForm
from .models import Mascota


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
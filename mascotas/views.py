
from django.shortcuts import render, redirect
from .forms import MascotaForm


def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_mascota')
    else:
        form = MascotaForm()

    return render(request, 'mascotas/registrar.html', {'form': form})

# Create your views here.

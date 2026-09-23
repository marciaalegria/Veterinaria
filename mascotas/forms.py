
from django import forms
from .models import Mascota


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'nombre_dueno']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()

        if not nombre:
            raise forms.ValidationError(
                "El nombre de la mascota es obligatorio."
            )

        return nombre

    def clean_especie(self):
        especie = self.cleaned_data['especie'].strip()

        if not especie:
            raise forms.ValidationError(
                "La especie es obligatoria."
            )

        return especie

    def clean_raza(self):
        raza = self.cleaned_data['raza'].strip()

        if not raza:
            raise forms.ValidationError(
                "La raza es obligatoria."
            )

        return raza

    def clean_nombre_dueno(self):
        nombre_dueno = self.cleaned_data['nombre_dueno'].strip()

        if not nombre_dueno:
            raise forms.ValidationError(
                "El nombre del dueño es obligatorio."
            )

        return nombre_dueno
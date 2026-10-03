from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    nombre_dueno = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

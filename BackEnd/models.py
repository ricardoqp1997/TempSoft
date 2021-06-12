from django.db import models


# Create your models here.
class Pais(models.Model):

    nombre_pais = models.CharField(
        verbose_name='País',
        max_length=20,
        unique=True,
    )

    REQUIRED_FIELDS = ['nombre_pais']

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre_pais


class Ciudad(models.Model):

    nombre_ciudad = models.CharField(
        verbose_name='Nombre de la ciudad',
        max_length=20,
        unique=True,
    )

    pais = models.ForeignKey(
        Pais,
        verbose_name='País',
        related_name='pais_nombre',
        on_delete=models.CASCADE
    )

    REQUIRED_FIELDS = [
        'nombre_ciudad',
        'pais'
    ]

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.nombre_ciudad


class TemperaturaHumedad(models.Model):

    ciudad = models.ForeignKey(
        Ciudad,
        verbose_name='Ciudad proveniente',
        on_delete=models.CASCADE
    )

    fecha_registro = models.DateTimeField(
        verbose_name='Fecha de registro',
        auto_now_add=True
    )

    temperatura = models.DecimalField(
        verbose_name='Temperatura',
        default=0.0,
        decimal_places=2,
        max_digits=20
    )

    humedad = models.DecimalField(
        verbose_name='Humedad',
        default=0.0,
        decimal_places=2,
        max_digits=20
    )

    REQUIRED_FIELDS = [
        'ciudad',
        'fecha_registro',
        'temperatura',
        'humedad'
    ]

    class Meta:
        verbose_name = 'Temperatura y humedad'
        verbose_name_plural = 'Temperaturas y humedades'

    def __str__(self):
        return self.ciudad.nombre_ciudad + ' | ' + str(self.fecha_registro)

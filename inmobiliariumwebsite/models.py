from django.db import models

# Create your models here.
class Inmueble(models.Model):
    TIPO_OPTIONS =  {
        'venta': 'venta',
        'alquiler': 'alquiler'
    }
    DESTINO_OPTIONS = {
        'vivienda': 'vivienda',
        'comercial': 'comercial'
    }

    name = models.CharField(
        max_length=50,
        default='Inmueble'
    )

    tipo = models.CharField(
        max_length=8,
        choices=TIPO_OPTIONS.items(),
        default='alquiler'
    )
    precio = models.DecimalField(
        max_digits=14,
        decimal_places=2
    )
    destino = models.CharField(
        max_length=9,
        choices=DESTINO_OPTIONS.items(),
        default='vivienda'
    )
    zona = models.CharField(
        max_length=50
    )
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes')
    activo = models.BooleanField(default=True)

    def __str__(self):
        # add id to the name
        return self.name + ' ' + str(self.id)
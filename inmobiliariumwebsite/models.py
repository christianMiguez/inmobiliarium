from django.db import models

class Inmueble(models.Model):
    TIPO_OPTIONS = {"venta": "venta", "alquiler": "alquiler"}
    DESTINO_OPTIONS = {
        "hawaii": "Hawaii",
        "caribe": "Caribe",
        "borabora": "Bora bora",
    }
    FINALIDAD = {
        'vivienda': 'vivienda',
        'comercial': 'comercial',
    }

    finalidad        = models.CharField( max_length=9, choices=FINALIDAD.items(), default='vivienda' )
    name             = models.CharField( max_length=50, default="Inmueble" )
    tipo             = models.CharField( max_length=8, choices=TIPO_OPTIONS.items(), default="alquiler" )
    precio           = models.DecimalField( max_digits=14, decimal_places=2, help_text="Siempre en DOLARES" )
    zona             = models.CharField( max_length=13, choices=DESTINO_OPTIONS.items(), default="hawaii" )
    descripcion      = models.CharField( max_length=200 )
    imagen_destacada = models.ImageField( upload_to="imagenes" )
    disponible       = models.BooleanField( default=True )
    piezas           = models.IntegerField( default=1 )
    banos            =  models.IntegerField( default=1 )
    garage           = models.BooleanField( default=False )
    area             = models.IntegerField( default=0, help_text="En metros cuadrados"  )
    es_destacado     = models.BooleanField( default=False)

    def __str__(self):
        return self.name + " " + str(self.name)


class InmuebleImagen(models.Model):
    inmueble    = models.ForeignKey( Inmueble, on_delete=models.CASCADE, related_name="galeria" )
    imagen      = models.ImageField( upload_to="galeria_inmuebles" )

    def __str__(self):
        return f"Imagen {self.id} ~ Inmueble: {self.inmueble.name}"

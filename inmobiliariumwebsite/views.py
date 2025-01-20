from django.shortcuts import render

from inmobiliariumwebsite.models import Inmueble, InmuebleImagen

def home(request):
    # destacadas = only 3
    destacadas = Inmueble.objects.filter(es_destacado=True)[:3]
    alazar = Inmueble.objects.order_by("?")[:3]
    print({
        'destacadas': destacadas,
        'alazar': alazar
    })
    return render(request, "index.html", {'destacadas': destacadas, 'alazar': alazar})

def busqueda(request):
    if 's' in request.GET and request.GET['s']:
        consulta = request.GET['s']
        propiedades = Inmueble.objects.filter(descripcion__contains=consulta)

        if not propiedades.exists():
            return render(request, "sin-resultados.html", {"consulta": consulta})


        imagenes = InmuebleImagen.objects.filter(inmueble=propiedades[0])
        print(imagenes[0].imagen)
        return render(request, "resultados.html", {'propiedades': propiedades, 'consulta': consulta, 'imagenes': imagenes})
    else:
        return render(request, "resultados.html")
    
def propiedad(request, id):
    propiedad = Inmueble.objects.get(id=id)
    if propiedad:
        print(propiedad)
        imagenes = InmuebleImagen.objects.filter(inmueble=propiedad)
        return render(request, "propiedad.html", {'propiedad': propiedad, 'imagenes': imagenes})
    
def buscar(request):
    return render(request, "buscar.html")
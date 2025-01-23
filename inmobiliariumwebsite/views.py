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
    
def propiedad(request, id):
    propiedad = Inmueble.objects.get(id=id)
    if propiedad:
        print(propiedad)
        imagenes = InmuebleImagen.objects.filter(inmueble=propiedad)
        return render(request, "propiedad.html", {'propiedad': propiedad, 'imagenes': imagenes})
    
def buscar(request):
    tipo = ''
    zona = ''
    piezas = 1
    banos = 1

    if 'tipo' in request.GET and request.GET['tipo']:
        tipo = request.GET['tipo']

    if 'zona' in request.GET and request.GET['zona']:
        zona = request.GET['zona']    

    if 'piezas' in request.GET and request.GET['piezas']:
        piezas = request.GET['piezas']
    
    if 'banos' in request.GET and request.GET['banos']:
        banos = request.GET['banos']

    if tipo == 'todos' and zona == 'todas' and piezas == '0' and banos == '0':
        propiedades = Inmueble.objects.all() 
    else:
        if tipo == 'todos' and zona == 'todas':
            propiedades = Inmueble.objects.filter(piezas=piezas, banos=banos)
        elif tipo == 'todos':
            propiedades = Inmueble.objects.filter(zona=zona, piezas=piezas, banos=banos)
        elif zona == 'todas':
            propiedades = Inmueble.objects.filter(tipo=tipo, piezas=piezas, banos=banos)
        else:
            propiedades = Inmueble.objects.filter(tipo=tipo, zona=zona, piezas=piezas, banos=banos)

    return render(request, "buscar.html", {'propiedades': propiedades})
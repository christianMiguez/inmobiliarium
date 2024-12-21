from django.shortcuts import render

from inmobiliariumwebsite.models import Inmueble

def home(request):
    return render(request, "index.html")

def busqueda(request):
    if 'busca' in request.GET and request.GET['busca']:
        consulta = request.GET['busca']
        propiedades = Inmueble.objects.filter(descripcion__contains=consulta)
        return render(request, "resultados.html", {'propiedades': propiedades, 'consulta': consulta})
    else:
        return render(request, "resultados.html")
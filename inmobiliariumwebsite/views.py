from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from inmobiliariumwebsite.forms import ContactoForm, CustomUserCreationForm
from inmobiliariumwebsite.models import Favorite, Inmueble, InmuebleImagen

def home(request):
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
    
    filtros = {}

    if tipo != 'todos':
        filtros['tipo'] = tipo
    if zona != 'todas':
        filtros['zona'] = zona
    if piezas != '0':
        filtros['piezas'] = piezas
    if banos != '0':
        filtros['banos'] = banos

    propiedades = Inmueble.objects.filter(**filtros)

    return render(request, "buscar.html", {'propiedades': propiedades})

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Correo desde Alohate'
            contenido = 'Mensaje de: ' + formulario.cleaned_data['nombre'] + '\n'
            contenido += 'Teléfono: ' + formulario.cleaned_data['telefono'] + '\n\n'
            contenido += formulario.cleaned_data['mensaje'] + '\n\n'
            contenido += 'Comunicarse al correo: ' + \
                formulario.cleaned_data['correo']
            mail = EmailMessage(titulo, contenido, to=['kisquian@gmail.com'])
            try:
                mail.send()
                print('Correo enviado')
                return HttpResponseRedirect('/contacto/?enviado=1')
            except:
                return render(request, 'correo_no_enviado.html')
    else:
        enviado = False
        if 'enviado' in request.GET:
            if request.GET['enviado'] == '1':
                enviado = True
        formulario = ContactoForm()
        return render(request, 'contacto.html', {'formulario': formulario, 'enviado': enviado})


def registro(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        try:
            formulario.save()
            
            query_params = "created_user=1"
            redirect_url = f"/login/?{query_params}"
            
            return redirect(redirect_url)

        except:
            print('Usuario 2')
            return render(request, 'registro.html', {'formulario': formulario})
    else:

        formulario = CustomUserCreationForm()
        return render(request, 'registro.html', {'formulario': formulario})
    
def error_404(request, exception):
    return render(request, '404.html',{})


def error_500(request):
    return render(request, '500.html', {})

def login_user(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('/?logged_user=1')
    elif request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            print(acceso)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return HttpResponseRedirect('/?logged_user=2')
            else:
                return render(request, 'login.html', {'formulario': formulario, 'error': 'Usuario o clave incorrectos'})
    else:
        created_user = False

        if 'created_user' in request.GET:
            if request.GET['created_user'] == '1':
                created_user = True
        formulario = AuthenticationForm()
        return render(request, 'login.html',{'formulario': formulario, 'created_user': created_user})


def salir(request):
    if not request.user.is_anonymous:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/')


@login_required
def a_favoritos(request, inmueble_id):
    
    print (inmueble_id)
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, inmueble=inmueble)

    if not created:
        favorite.delete()  # If it already exists, remove it (toggle behavior)
        print('Eliminado')
        return redirect(f'/mis_favoritos/?favorito=0')
    else:
            return redirect(f'/mis_favoritos/?favorito=1')

@login_required
def mis_favoritos(request):
    favoritos = Favorite.objects.filter(user=request.user)
    propiedades = [fav.inmueble for fav in favoritos]
    favorito = None

    if 'favorito' in request.GET:
        if request.GET['favorito'] == '1':
            favorito = True
        elif request.GET['favorito'] == '0':
            favorito = False
    return render(request, 'mis-favoritos.html', {'propiedades': propiedades, 'favorito': favorito})
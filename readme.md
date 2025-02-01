# Alohate

TODO: 
[ ] - agregar login page c/funcionalidad
[ ] - agregar register page c/funcionalidad
[ ] - agregar contact form c/funcionalidad
[ ] - agregar favoritos c/funcionalidad
[ ] - Confetti al alquilar/comprar

Alohate is a Django-based web application for managing hawaii and caribbean real estate listings. This project allows users to browse, search, and filter real estate listings. This is the typical CRUD app where superusers can create, read, update, and delete properties.

The first time after you execute django-admin startproyect Alohate, you need to do the following steps:

1. add import os en settings.py
2. create templates, static folder
3. In settings specify static, templates, etc paths:


```
- TIME_ZONE
```

```
- STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

```
- (dirs) TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        (...)
```

4. python3 manage.py startapp inmobiliariumwebsite (or whatever you want to call it)

This inmobiliariumwebsite app will contain the models, views, and templates for the project.

5. en installed_apps add the app

```
- INSTALLED_APPS = [
    'inmobiliariumwebsite',
    (...)
```

6. Create models in models.py

7. Create views in views.py

8. Create urls in urls.py

9. run python3 manage.py makemigrations

10. run python3 manage.py migrate

11. run python3 manage.py createsuperuser. for dev we are using: 
chris
ChrisPass101

12. in admin.py register the models by doing:


/// favoritos

Para agregar una funcionalidad de favoritos a tu sistema, puedes crear un nuevo modelo que vincule a los usuarios con los inmuebles que marquen como favoritos. Esto se logra utilizando una relación ManyToManyField entre el modelo de usuario y el modelo Inmueble. A continuación, se detalla cómo implementar esto:

Paso 1: Agregar el modelo de favoritos
python
Copiar código
from django.contrib.auth.models import User
from django.db import models

class InmuebleFavorito(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='favoritos'
    )
    inmueble = models.ForeignKey(
        Inmueble, 
        on_delete=models.CASCADE, 
        related_name='favoritos'
    )
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'inmueble')

    def __str__(self):
        return f"{self.user.username} - {self.inmueble.name}"
Explicación del modelo
Relación con User: Usamos un ForeignKey para vincular cada favorito a un usuario registrado.
Relación con Inmueble: Usamos otro ForeignKey para vincular el inmueble que el usuario marca como favorito.
unique_together: Esto asegura que un usuario no pueda agregar el mismo inmueble más de una vez a sus favoritos.
fecha_agregado: Opcionalmente, puedes agregar un campo para registrar cuándo se agregó el inmueble a favoritos.
Paso 2: Migraciones
Después de agregar el modelo, genera y aplica las migraciones:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Paso 3: Funcionalidad en la Vista
Puedes crear una vista para que los usuarios marquen un inmueble como favorito o lo eliminen de su lista de favoritos. Ejemplo:

python
Copiar código
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Inmueble, InmuebleFavorito

@login_required
def toggle_favorito(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    favorito, created = InmuebleFavorito.objects.get_or_create(
        user=request.user, 
        inmueble=inmueble
    )
    if not created:
        favorito.delete()
    return redirect('nombre_de_tu_vista')
Paso 4: Mostrar Favoritos en la Plantilla
Puedes mostrar los favoritos de un usuario en una página o destacar si un inmueble ya está marcado como favorito.

python
Copiar código
@login_required
def listar_favoritos(request):
    favoritos = InmuebleFavorito.objects.filter(user=request.user)
    return render(request, 'favoritos.html', {'favoritos': favoritos})
Plantilla favoritos.html:

html
Copiar código
<h2>Mis Favoritos</h2>
<ul>
    {% for favorito in favoritos %}
        <li>
            {{ favorito.inmueble.name }} - {{ favorito.inmueble.precio }}
            <a href="{% url 'toggle_favorito' favorito.inmueble.id %}">Eliminar de favoritos</a>
        </li>
    {% endfor %}
</ul>
Paso 5: Añadir Botón de Favoritos
En la plantilla donde muestras los inmuebles, puedes agregar un botón para marcar o desmarcar favoritos:

html
Copiar código
{% for inmueble in inmuebles %}
    <div>
        <h3>{{ inmueble.name }}</h3>
        <p>{{ inmueble.descripcion }}</p>
        <a href="{% url 'toggle_favorito' inmueble.id %}">
            {% if inmueble.favoritos.filter(user=request.user).exists %}
                Quitar de Favoritos
            {% else %}
                Añadir a Favoritos
            {% endif %}
        </a>
    </div>
{% endfor %}
Esto verifica si el inmueble ya está en los favoritos del usuario para mostrar el texto adecuado.

Paso 6: URLs
Añade las rutas en tu archivo urls.py:

python
Copiar código
from django.urls import path
from . import views

urlpatterns = [
    path('favoritos/toggle/<int:inmueble_id>/', views.toggle_favorito, name='toggle_favorito'),
    path('favoritos/', views.listar_favoritos, name='listar_favoritos'),
]
Con estos pasos, tendrás una funcionalidad completa para que los usuarios puedan marcar y administrar favoritos en tu sitio de bienes raíces. 🚀

//////////////

"""
URL configuration for inmobiliarium project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from inmobiliariumwebsite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('buscar', buscar, name='buscar'),
    path('propiedad/<int:id>/', propiedad, name='propiedad'),
    path('contacto/',contacto, name='contacto'),
    path('registro/', registro, name='registro'),
    path('login/', login_user, name='login'),
    path('logout/', salir, name='logout'),
    path('contacto/', contacto, name='contacto'),
    path('add_to_fav/<int:inmueble_id>/', a_favoritos, name='add_to_fav'),
    path('mis_favoritos/', mis_favoritos, name='mis_favoritos'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

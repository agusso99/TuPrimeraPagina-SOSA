from django.shortcuts import render
from .models import Proyecto, Publicacion, Contacto


def index(request):
    return render(request, "Blog/index.html")

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "Blog/proyecto.html", {"proyectos": proyectos})

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, "Blog/publicaciones.html", {"publicaciones": publicaciones})

def mensajes(request):
    contactos = Contacto.objects.all()
    return render(request, "Blog/contacto.html", {"contactos": contactos})

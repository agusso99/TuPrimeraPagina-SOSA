from django.shortcuts import render, redirect
from .models import Proyecto, Publicacion, Contacto
from .forms import ContactoForm


def index(request):
    return render(request, "Blog/index.html")

def lista_proyectos(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        proyectos = Proyecto.objects.filter(titulo__icontains=busqueda)
    else:
        proyectos = Proyecto.objects.all()
    return render(request, "Blog/proyecto.html", {"proyectos": proyectos})

def lista_publicaciones(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        publicaciones = Publicacion.objects.filter(titulo__icontains=busqueda)
    else:
        publicaciones = Publicacion.objects.all()
    return render(request, "Blog/publicaciones.html", {"publicaciones": publicaciones})

def mensajes(request):
    contactos = Contacto.objects.all()
    return render(request, "Blog/contacto.html", {"contactos": contactos})

def crear_mensaje(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            print("Su mensaje fue enviado.")
            form.save()
            return redirect("crear_mensajes")
    else:
        form = ContactoForm()
    return render(request, "Blog/contacto.html", {"form": form})

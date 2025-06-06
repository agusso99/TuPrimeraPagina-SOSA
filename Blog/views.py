from django.shortcuts import render, redirect
from .models import Proyecto, Publicacion, Contacto
from .forms import ContactoForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib import messages

def index(request):
    #if request.user.is_authenticated:
        #return redirect('lista_proyectos')
    return render(request, "Blog/index.html")

class ProyectoListView(ListView):
    model = Proyecto
    template_name = "Blog/proyecto.html"
    context_object_name = "proyectos"

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            return Proyecto.objects.filter(
                Q(titulo__icontains=q) | Q(autor__username__icontains=q)
            )
        return Proyecto.objects.all()

class PublicacionListView(ListView):
    model = Publicacion
    template_name = "Blog/publicaciones.html"
    context_object_name = "publicaciones"

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            return Publicacion.objects.filter(
                Q(titulo__icontains=q) | Q(autor__username__icontains=q)
            )
        return Publicacion.objects.all()

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    template_name = "Blog/proyecto_form.html"
    fields = ['titulo', 'genero', 'descripcion', 'fecha_lanzamiento', 'duracion', 'imagen']
    success_url = reverse_lazy('lista_proyectos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    template_name = "Blog/proyecto_form.html"
    fields = ['titulo', 'genero', 'descripcion', 'fecha_lanzamiento', 'duracion', 'imagen']
    success_url = reverse_lazy('lista_proyectos')

    def dispatch(self, request, *args, **kwargs):
        proyecto = self.get_object()
        if proyecto.autor != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = "Blog/proyecto_confirm_delete.html"
    success_url = reverse_lazy('lista_proyectos')

    def dispatch(self, request, *args, **kwargs):
        proyecto = self.get_object()
        if proyecto.autor != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = "Blog/proyecto_detail.html"
    context_object_name = "proyecto"

class PublicacionCreateView(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = "Blog/publicacion_form.html"
    fields = ['titulo', 'contenido', 'proyecto_relacionado']
    success_url = reverse_lazy('lista_publicaciones')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['proyecto_relacionado'].queryset = Proyecto.objects.filter(autor=self.request.user)
        return form

class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = "Blog/publicacion_form.html"
    fields = ['titulo', 'contenido', 'proyecto_relacionado']
    success_url = reverse_lazy('lista_publicaciones')

    def dispatch(self, request, *args, **kwargs):
        publicacion = self.get_object()
        if publicacion.autor != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = "Blog/publicacion_confirm_delete.html"
    success_url = reverse_lazy('lista_publicaciones')

    def dispatch(self, request, *args, **kwargs):
        publicacion = self.get_object()
        if publicacion.autor != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PublicacionDetailView(DetailView):
    model = Publicacion
    template_name = "Blog/publicacion_detail.html"
    context_object_name = "publicacion"

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

def profile(request):
    return render(request, 'accounts/profile.html')

def about_view(request):
    return render(request, 'Blog/about.html')

from django.contrib import admin
from .models import Proyecto, Publicacion, Contacto


#admin.site.register(Proyecto)
#admin.site.register(Publicacion)
#admin.site.register(Contacto)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "descripcion", "fecha_lanzamiento", "duracion", "genero"]
    list_filter = ["titulo"]
    ordering = ["-fecha_lanzamiento"]

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ["titulo", "contenido", "fecha", "proyecto_relacionado"]
    ordering = ["-fecha"]

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "email", "mensaje", "fecha_envio", "estado"]
    ordering = ["-fecha_envio"]

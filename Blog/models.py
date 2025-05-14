from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    duracion = models.DurationField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titulo} - Lanzamiento: {self.fecha_lanzamiento}."


class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    proyecto_relacionado = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    class Estado(models.TextChoices):
        LEIDO = "Visto", "Leido"
        NO_LEIDO = "Sin Ver", "No Leido"
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.NO_LEIDO)

    def __str__(self):
        return f"Tenes un mensaje de {self.nombre} / {self.email}."
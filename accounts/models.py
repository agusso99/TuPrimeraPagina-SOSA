from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'


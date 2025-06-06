from django.urls import path
from .views import foro_view

urlpatterns = [
    path('', foro_view, name='foro'),
]
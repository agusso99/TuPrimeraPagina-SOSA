from django.urls import path
from . import views

urlpatterns = [
    path('proyectos/', views.ProyectoListView.as_view(), name='lista_proyectos'),
    path('proyectos/crear/', views.ProyectoCreateView.as_view(), name='crear_proyecto'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='detalle_proyecto'),
    path('proyectos/<int:pk>/editar/', views.ProyectoUpdateView.as_view(), name='modificar_proyecto'),
    path('proyectos/<int:pk>/eliminar/', views.ProyectoDeleteView.as_view(), name='eliminar_proyecto'),
    path('publicaciones/', views.PublicacionListView.as_view(), name='lista_publicaciones'),
    path('publicaciones/crear/', views.PublicacionCreateView.as_view(), name='crear_publicacion'),
    path('publicaciones/<int:pk>/', views.PublicacionDetailView.as_view(), name='detalle_publicacion'),
    path('publicaciones/<int:pk>/editar/', views.PublicacionUpdateView.as_view(), name='modificar_publicacion'),
    path('publicaciones/<int:pk>/eliminar/', views.PublicacionDeleteView.as_view(), name='eliminar_publicacion'),
]
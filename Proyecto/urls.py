"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from Blog import views
from django.conf import settings
from django.conf.urls.static import static
from Blog.views import ProyectoListView, PublicacionListView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyectos/', include('Blog.urls')),
    path('publicaciones/', PublicacionListView.as_view(), name="lista_publicaciones"),
    path('contacto/', views.crear_mensaje, name="crear_mensajes"),
    path('about/', views.about_view, name="about"),
    path("", views.index, name="index"),
    path('accounts/', include('accounts.urls')),
    path('accounts/profile/', views.profile, name="profile"),
    path('foro/', include('foro.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
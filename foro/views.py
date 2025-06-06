from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm
from django.contrib import messages

@login_required
def foro_view(request):
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')
    mensajes_enviados = Mensaje.objects.filter(emisor=request.user).order_by('-fecha')
    form = MensajeForm(user=request.user)

    if request.method == 'POST':
        form = MensajeForm(request.POST, user=request.user)
        if form.is_valid():
            nuevo_mensaje = form.save(commit=False)
            nuevo_mensaje.emisor = request.user
            nuevo_mensaje.save()
            return redirect('foro')

    return render(request, 'foro/foro.html', {
        'mensajes_recibidos': mensajes_recibidos,
        'mensajes_enviados': mensajes_enviados,
        'form': form
    })
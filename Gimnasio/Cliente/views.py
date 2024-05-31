from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profesor, TipoEntrenamiento, Turno, Cliente
from .forms import ReservaTurnoForm
import datetime


@login_required
def cliente_detalle(request):
    if hasattr(request.user, 'cliente'):
        cliente = request.user.cliente
        return render(request, 'Cliente/cliente_detalle.html')
    else:
        return redirect('paginaprincipal')

def paginaprincipal(request):
    return render(request, 'Cliente/paginaprincipal.html')

def opcion_entrenamiento(request):
    entrenamientos = TipoEntrenamiento.objects.all()
    return render(request, 'Cliente/opcion_entrenamiento.html', {'entrenamientos': entrenamientos})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'Cliente/profesores.html', {'profesores': profesores})

def about_me(request):
    return render(request, 'Cliente/about_me.html')

def inscripcion_entrenamiento(request, entrenamiento_id):
    entrenamiento = get_object_or_404(TipoEntrenamiento, id=entrenamiento_id)
    return redirect('index')


def turno(request):
    horarios = {
        'Lunes a Viernes': ('06:00', '22:00'),
        'Sábados': ('08:00', '20:00'),
        'Domingos': ('09:00', '18:00')
    }

    if request.method == 'POST':
        form = ReservaTurnoForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('Cliente/turno.html')
    else:
        form = ReservaTurnoForm()

    context = {
        'horarios': horarios,
        'form': form
    }
    return render(request, 'Cliente/turno.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profesor, TipoEntrenamiento, Turno, Cliente

@login_required
def cliente_detalle(request):
    cliente = get_object_or_404(Cliente, usuario=request.user)
    return render(request, 'Cliente/cliente_detalle.html', {'cliente': cliente})

def paginaprincipal(request):
    return render(request, 'Cliente/paginaprincipal.html')

def opcion_entrenamiento(request):
    entrenamientos = TipoEntrenamiento.objects.all()
    return render(request, 'Cliente/opcion_entrenamiento.html', {'entrenamientos': entrenamientos})

@login_required
def turno(request):
    if request.method == 'POST':
        pass
    turnos = Turno.objects.filter(usuario=request.user)
    return render(request, 'Cliente/turno.html', {'turnos': turnos})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'Cliente/profesores.html', {'profesores': profesores})

def about_me(request):
    return render(request, 'Cliente/about_me.html')


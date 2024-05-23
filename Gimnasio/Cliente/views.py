from django.shortcuts import render, redirect

# Create your views here.

from .models import Cliente, Turno

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente})

def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        Cliente.objects.create(nombre=nombre, edad=edad)
        return redirect('lista_clientes')
    return render(request, 'cliente/crear_cliente.html')

def eliminar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')

def about(request):
    return render(request, 'cliente/about.html')

def home(request):
    return render(request, 'cliente/home.html')


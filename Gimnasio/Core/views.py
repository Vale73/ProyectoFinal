from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from .models import Usuario

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('admin_view')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def admin_view(request):
    if request.user.user_type != 'admin':
        return redirect('login')
    usuarios = Usuario.objects.all()
    return render(request, 'core/admin.html', {'usuarios': usuarios})

@login_required
def user_crud_view(request, user_id=None):
    if request.user.user_type != 'admin':
        return redirect('login')
    if user_id:
        user = Usuario.objects.get(id=user_id)
    else:
        user = None
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_view')
    else:
        form = RegistroForm(instance=user)
    return render(request, 'core/user_crud.html', {'form': form, 'user': user})


def home_view(request):
    return render(request, 'core/home.html')



from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def index(request):

    return render(request, 'index.html',
    )

def galeria(request):

    return render(request, 'GaleriaFotos.html',
    )

def crearUsuario(request):
    if request.method=='POST': 
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('index')
    else:
        usuario_form= UsuarioForm()
    return render(request, 'core/form_crearusuario.html', {'usuario_form': usuario_form})
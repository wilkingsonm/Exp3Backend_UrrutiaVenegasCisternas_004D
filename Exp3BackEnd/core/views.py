from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def home(request):
    nombre = 'Jorge Venegas'
    
    usuarios = Usuario.objects.all()  #similar al comando select

    return render(request, 'home.html', context={'nom_usuario': nombre, 'datos': usuarios},
    )

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
            return redirect('home')
    else:
        usuario_form= UsuarioForm()
    return render(request, 'core/form_crearusuario.html', {'usuario_form': usuario_form})

def Ver(request):
    usuarios = Usuario.objects.all()

    return render(request, 'core/ver.html', context={'usuarios':usuarios})



def form_mod_usuario(request,id):
    usuario = Usuario.objects.get(correo=id)

    datos ={
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST': 
        formulario = UsuarioForm(data=request.POST, instance = usuario)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('ver')
    return render(request, 'core/form_mod_usuario.html', datos)

from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def galeria(request):

    return render(request, 'GaleriaFotos.html',
    )

def registro(request):

    return render(request, 'core/Registro.html',
    )
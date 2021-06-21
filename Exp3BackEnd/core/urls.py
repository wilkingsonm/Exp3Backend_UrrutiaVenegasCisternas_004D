from django.urls import path
from .views import index,galeria,crearUsuario

urlpatterns = [

    path('', index, name="index"),
    path('galeria', galeria, name="galeria"),
    path('crear_usuario', crearUsuario, name="crearUsuario"),
]
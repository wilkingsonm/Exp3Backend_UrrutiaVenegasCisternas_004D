from django.urls import path
from .views import home,index,galeria,crearUsuario,Ver,form_mod_usuario

urlpatterns = [

    path('home', home, name="home"),
    path('', index, name="index"),
    path('galeria', galeria, name="galeria"),
    path('crear_usuario', crearUsuario, name="crearUsuario"),
    path('ver', Ver, name="ver"),
    path('form_mod_usuario/<id>', form_mod_usuario, name="form_mod_usuario"),
]
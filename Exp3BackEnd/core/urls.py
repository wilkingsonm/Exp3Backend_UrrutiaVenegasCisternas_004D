from django.urls import path
from django.urls.resolvers import URLPattern
from .views import galeria, index, registro

urlpatterns = [

    path('', index, name="index"),
    path('galeria', galeria, name="galeria"),
    path('registro', registro, name="registro"),
]
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria(models.Model):

    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')

    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de Categoria')



    def __str__(self):

        return (self.nombreCategoria)


class Usuario(models.Model):

    correo = models.CharField(max_length=100, primary_key=True, verbose_name='Correo')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    motivo = models.CharField(max_length=150, verbose_name='Motivo')
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)



    def __str__(self):

        return (self.correo)
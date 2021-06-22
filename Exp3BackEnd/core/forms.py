from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Usuario

class UsuarioForm(forms.ModelForm):

    class Meta: 
        model= Usuario
        fields = ['correo', 'nombre', 'motivo', 'categoria']
        labels ={
            'correo': 'Correo', 
            'nombre': 'Nombre', 
            'motivo': 'Motivo', 
            'categoria': 'Categoría',
        }
        widgets={
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'motivo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese motivo', 
                    'id': 'motivo'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

        

from django import forms
from django.contrib.auth.models import User
from wsgiref.validate import validator
from django.core import validators
from .models import Categoria, Producto

class CategoriaRegistroForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre", required=True)
    description = forms.CharField(max_length=100, label="Descripción", required=True)

    name.widget.attrs['class'] = 'form-control'
    description.widget.attrs['class'] = 'form-control'

    name.label= "Nombre"
    description.label= "Descripción"

class CategoriaRegistroForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name', 'description']

    name = forms.CharField(max_length=100, label="Nombre", required=True)
    description = forms.CharField(max_length=100, label="Descripción", required=True)
    
    name.widget.attrs['class'] = 'form-control'
    description.widget.attrs['class'] = 'form-control'

    name.label= "Nombre"
    description.label= "Descripción"

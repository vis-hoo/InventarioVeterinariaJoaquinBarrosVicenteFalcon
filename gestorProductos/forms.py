from django import forms

from .models import Categoria, Producto

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

class CategoriaEditarForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name', 'description']

    name = forms.CharField(max_length=100, label="Nombre", required=True)
    description = forms.CharField(max_length=100, label="Descripción", required=True)
    
    name.widget.attrs['class'] = 'form-control'
    description.widget.attrs['class'] = 'form-control'

    name.label= "Nombre"
    description.label= "Descripción"

class ProductoRegistroForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'description', 'price', 'category']

    name = forms.CharField(max_length=100, label="Nombre", required=True)
    description = forms.CharField(max_length=100, label="Descripción", required=True)
    price = forms.IntegerField(min_value=0, label="Precio", required=True)
    category = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        label="Categoría",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control form-control-user'}),
        empty_label="Seleccione una categoría"
    )
    
    name.label= "Nombre"
    description.label= "Descripción"
    price.label= "Precio"
    category.label= "Categoría"

class ProductoEditarForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'description', 'price', 'category']
    
    name = forms.CharField(max_length=100, label="Nombre", required=True)
    description = forms.CharField(max_length=100, label="Descripción", required=True)
    price = forms.IntegerField(min_value=0, label="Precio", required=True)
    category = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        label="Categoría",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control form-control-user'}),
        empty_label="Seleccione una categoría"
    )

    name.label= "Nombre"
    description.label= "Descripción"
    price.label= "Precio"
    category.label= "Categoría"

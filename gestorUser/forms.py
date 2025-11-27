from django import forms
from django.contrib.auth.models import User
from wsgiref.validate import validator
from django.core import validators

class UsuarioRegistroForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="Nombre", required=True)
    last_name = forms.CharField(max_length=100, label="Apellido", required=True)
    email = forms.EmailField(label="Correo Electrónico", required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Contraseña", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Contraseña", required=True)

    first_name.widget.attrs['class'] = 'form-control'
    last_name.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    password1.widget.attrs['class'] = 'form-control'
    password2.widget.attrs['class'] = 'form-control'

    first_name.label= "Nombre"
    last_name.label= "Apellido"
    email.label= "Email"
    password1.label= "Contraseña"
    password2.label= "Confirmar Contraseña"

class UsuarioRegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    first_name = forms.CharField(max_length=100, label="Nombre", required=True)
    last_name = forms.CharField(max_length=100, label="Apellido", required=True)
    email = forms.EmailField(label="Correo Electrónico", required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Contraseña", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Contraseña", required=True)
    
    first_name.widget.attrs['class'] = 'form-control'
    last_name.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    password1.widget.attrs['class'] = 'form-control'
    password2.widget.attrs['class'] = 'form-control'

    first_name.label= "Nombre"
    last_name.label= "Apellido"
    email.label= "Email"
    password1.label= "Contraseña"
    password2.label= "Confirmar Contraseña"

class UsuarioUsernameChangeForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nombre de usuario", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña", required=True)

    username.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'

    username.label= "Nombre de usuario"
    password.label= "Contraseña"

class UsuarioUsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(max_length=100, label="Nombre de usuario", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña", required=True)
    
    username.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'

    username.label= "Nombre de usuario"
    password.label= "Contraseña"
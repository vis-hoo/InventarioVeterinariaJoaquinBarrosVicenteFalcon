from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    form = UsuarioRegistroForm()
    
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['first_name'] + form.cleaned_data['last_name'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password1']
                )
                user.is_staff = False
                user.is_superuser = False
                user.save()
                messages.success(request, "Usuario registrado exitosamente")
                return HttpResponseRedirect(reverse('login'))

            except IntegrityError:
                messages.error(request, "Ya existe un usuario con el mismo nombre o correo.")
                return HttpResponseRedirect(reverse('signup'))
    data = {'form': form}
    return render(request, 'registration/signup.html', data)

@login_required
def home_panel(request):
    return render(request, 'user_views/home_panel.html')

@login_required
def username_change(request):
    form = UsuarioUsernameChangeForm()
    
    if request.method == 'POST':
        form = UsuarioUsernameChangeForm(request.POST)
        if form.is_valid():
            try:
                for user in User.objects.all():
                    if user.username == form.cleaned_data['username']:
                        messages.error(request, "Ya existe un usuario con el mismo nombre de usuario.")
                        return HttpResponseRedirect(reverse('username_change'))

                if not request.user.check_password(form.cleaned_data['password']):
                    messages.error(request, "Contraseña incorrecta.")
                    return HttpResponseRedirect(reverse('username_change'))

                user = request.user
                user.username = form.cleaned_data['username']
                user.save()
                messages.success(request, "Nombre de usuario cambiado exitosamente")
                return HttpResponseRedirect(reverse('home_panel'))

            except IntegrityError:
                messages.error(request, "Ya existe un usuario con el mismo nombre de usuario.")
                return HttpResponseRedirect(reverse('username_change'))
    data = {'form': form}
    return render(request, 'user_views/user_settings/username_change.html')

@login_required
def email_change(request):
    form = UsuarioEmailChangeForm()
    
    if request.method == 'POST':
        form = UsuarioEmailChangeForm(request.POST)
        if form.is_valid():
            try:
                for user in User.objects.all():
                    if user.email == form.cleaned_data['email']:
                        messages.error(request, "Ya existe un usuario con el mismo correo electrónico.")
                        return HttpResponseRedirect(reverse('email_change'))

                if not request.user.check_password(form.cleaned_data['password']):
                    messages.error(request, "Contraseña incorrecta.")
                    return HttpResponseRedirect(reverse('email_change'))

                user = request.user
                user.email = form.cleaned_data['email']
                user.save()
                messages.success(request, "Correo electrónico cambiado exitosamente")
                return HttpResponseRedirect(reverse('home_panel'))

            except IntegrityError:
                messages.error(request, "Ya existe un usuario con el mismo correo electrónico.")
                return HttpResponseRedirect(reverse('email_change'))
    data = {'form': form}
    return render(request, 'user_views/user_settings/email_change.html')


@login_required
def password_change(request):
    form = UsuarioPasswordChangeForm()
    
    if request.method == 'POST':
        form = UsuarioPasswordChangeForm(request.POST)
        if form.is_valid():
            try:
                if not request.user.check_password(form.cleaned_data['password']):
                    messages.error(request, "Contraseña incorrecta.")
                    return HttpResponseRedirect(reverse('password_change'))

                if form.cleaned_data['new_password'] != form.cleaned_data['new_password_confirmation']:
                    messages.error(request, "Las contraseñas no coinciden.")
                    return HttpResponseRedirect(reverse('password_change'))

                user = request.user
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                messages.success(request, "Contraseña cambiada exitosamente")
                return HttpResponseRedirect(reverse('home_panel'))

            except IntegrityError:
                messages.error(request, "Error al cambiar la contraseña.")
                return HttpResponseRedirect(reverse('password_change'))
    data = {'form': form}
    return render(request, 'user_views/user_settings/password_change.html')
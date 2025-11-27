from .form import UsuarioRegistroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home_page.html')

@login_required
def user_home(request):
    return render(request, 'user_home.html')

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

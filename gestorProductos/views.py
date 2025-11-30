from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

@login_required
@user_passes_test(lambda u: u.is_superuser)
def categories_list(request):
    categorias = Categoria.objects.all()
    data = {'categorias': categorias}
    return render(request, 'user_views/super_user/categories_control/categories_list.html', data)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def categories_create(request):
    form = CategoriaRegistroForm()
    
    if request.method == 'POST':
        form = CategoriaRegistroForm(request.POST)
        if form.is_valid():
            try:
                for categoria in Categoria.objects.all():
                    if categoria.nombre == form.cleaned_data['name']:
                        messages.error(request, "Ya existe una categoría con el mismo nombre.")
                        return HttpResponseRedirect(reverse('categories_create'))

                categoria = Categoria.objects.create(
                    nombre = form.cleaned_data['name'],
                    descripcion = form.cleaned_data['description']
                )
                categoria.save()
                messages.success(request, "Categoría creada exitosamente")
                return HttpResponseRedirect(reverse('home_panel'))

            except IntegrityError:
                messages.error(request, "Ya existe una categoría con el mismo nombre.")
                return HttpResponseRedirect(reverse('categories_create'))
    data = {'form': form}
    return render(request, 'user_views/super_user/categories_control/categories_create.html', data)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def categories_edit(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaEditarForm(instance=categoria)

    if request.method == 'POST':
        form = CategoriaEditarForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria.nombre = form.cleaned_data['name']
            categoria.descripcion = form.cleaned_data['description']
            categoria.save()
            messages.success(request, "Categoría editada exitosamente")
            return HttpResponseRedirect(reverse('categories_list'))

    data = {'form': form, 'cat': categoria}
    return render(request, 'user_views/super_user/categories_control/categories_edit.html', data)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def categories_delete(request, id): 
    Categoria.objects.get(id=id).delete()
    messages.success(request, "Categoría eliminada exitosamente")
    return HttpResponseRedirect(reverse('categories_list'))

@login_required
def products_list(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'user_views/products_control/products_list.html', data)

@login_required
def products_create(request):
    form = ProductoRegistroForm()
    
    if request.method == 'POST':
        form = ProductoRegistroForm(request.POST)
        if form.is_valid():
            try:
                for producto in Producto.objects.all():
                    if producto.nombre == form.cleaned_data['name']:
                        messages.error(request, "Ya existe un producto con el mismo nombre.")
                        return HttpResponseRedirect(reverse('products_create'))

                producto = Producto.objects.create(
                    nombre = form.cleaned_data['name'],
                    descripcion = form.cleaned_data['description'],
                    precio = form.cleaned_data['price'],
                    categoria = form.cleaned_data['category'],
                    creador = request.user
                )
                producto.save()
                messages.success(request, "Producto creado exitosamente")
                return HttpResponseRedirect(reverse('products_list'))

            except IntegrityError:
                messages.error(request, "Ya existe un producto con el mismo nombre.")
                return HttpResponseRedirect(reverse('products_create'))
    data = {'form': form}
    return render(request, 'user_views/products_control/products_create.html', data)

@login_required
def products_edit(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoEditarForm(instance=producto)

    if request.method == 'POST':
        form = ProductoEditarForm(request.POST, instance=producto)
        if form.is_valid():
            producto.nombre = form.cleaned_data['name']
            producto.descripcion = form.cleaned_data['description']
            producto.precio = form.cleaned_data['price']
            producto.categoria = form.cleaned_data['category']
            producto.save()
            messages.success(request, "Producto editado exitosamente")
            return HttpResponseRedirect(reverse('products_list'))

    data = {'form': form, 'prod': producto}
    return render(request, 'user_views/products_control/products_edit.html', data)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def products_delete(request, id): 
    Producto.objects.get(id=id).delete()
    messages.success(request, "Producto eliminado exitosamente")
    return HttpResponseRedirect(reverse('products_list'))

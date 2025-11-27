"""
URL configuration for InventarioVeterinariaJoaquinBarrosVicenteFalcon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestorUser.views import *
from gestorProductos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('home_panel/', home_panel, name='home_panel'),

    path('username_change/', username_change, name='username_change'),
    path('email_change/', email_change, name='email_change'),
    path('password_change/', password_change, name='password_change'),
    
    path('categories_list/', categories_list, name='categories_list'),
    path('categories_create/', categories_create, name='categories_create'),
    path('categories_edit/<int:id>/', categories_edit, name='categories_edit'),
    path('categories_delete/<int:id>/', categories_delete, name='categories_delete'),
]

from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

from django.contrib.auth.models import User
from django.db import models
from django.db.models import query
from django.db.models.expressions import OrderBy
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.descripcion}"

class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    precio = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria")
    imagen = models.FileField(upload_to='imagenes/')
    descripcion = models.CharField(max_length=500)
    fecha_publicacion = models.DateField(null=False, default=timezone.now())

    def __str__(self):
        return f"{self.nombre}"


from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from sitio.models import Producto

# Create your models here.

class Carrito(models.Model):
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carrito=self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"]={}
        self.carrito=carrito

    def agregar(self, producto):
        if (str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardar()
    
    def guardar(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar()
    
    def quitar(self, producto):
        for key, value in self.carrito.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-producto.precio
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True

from sitio.models import Producto, Categoria
from django.shortcuts import redirect, render, get_object_or_404
from .models import Carrito
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def carrito(request):  
        carrito=Carrito(request)
        return render(request, 'carrito/carrito.html', {
            "lista_categorias": Categoria.objects.all()
        })

def agregar(request, producto_id):
    carrito=Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.agregar(producto=producto)
    return redirect('carrito:carrito')

def quitar(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.quitar(producto=producto)
    return redirect('carrito:carrito')

def eliminar(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect('carrito:carrito')

def limpiar(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('sitio:index')
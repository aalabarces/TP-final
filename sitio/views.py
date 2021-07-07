from django.contrib.auth import forms
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import FormProducto
from carrito.models import Carrito

# Create your views here.
def index(request):

    return render(request, 'sitio/index.html', {
        "lista_productos": Producto.objects.all(),
        "lista_categorias": Categoria.objects.all(),

    })

def producto(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    return render(request, "sitio/producto.html", {
        "producto": un_producto,
        "lista_categorias": Categoria.objects.all()
    })

def producto_nuevo(request):
    if request.user.is_staff:    
        if request.method == "POST":
            form = FormProducto(request.POST, request.FILES, instance=Producto(imagen=request.FILES['imagen']))
            if form.is_valid():
                form.save()
                return redirect("sitio:index")
        else:
            form = FormProducto(initial={'fecha_publicacion':timezone.now()})
            return render(request, 'sitio/producto_nuevo.html', {
                "lista_categorias": Categoria.objects.all(),
                "form": form
            })
    else:
        raise Http404()


def producto_editar(request, producto_id):
    if request.user.is_staff:
        un_producto = get_object_or_404(Producto, id=producto_id)
        if request.method == "POST":  
            user = User.objects.get(username=request.user)
            form = FormProducto(data=request.POST, files=request.FILES, instance=un_producto)
            if form.is_valid():
                form.save()
                return redirect("sitio:index")
        else:
            form = FormProducto(instance = un_producto)
            return render(request, 'sitio/producto_editar.html', {
                "producto": un_producto,
                "form": form,
                "lista_categorias": Categoria.objects.all()
            })
    else:
        raise Http404()

def producto_eliminar(request, producto_id):
    if request.user.is_staff:
        un_producto = get_object_or_404(Producto, id=producto_id)
        un_producto.delete()
        return redirect("sitio:index")
    else:
        raise Http404()

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('sitio:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def acercade(request):
    return render(request, "sitio/acercade.html", {
        "lista_categorias": Categoria.objects.all()
    })

def contacto(request):
    if request.method == 'POST':
        return redirect("sitio:index")
    return render(request, "sitio/contacto.html", {
        "lista_categorias": Categoria.objects.all()
    })

def filtro_categorias(request, categ_id):
    una_categ = get_object_or_404(Categoria, id=categ_id)
    queryset = Producto.objects.all()
    queryset = queryset.filter(categoria=una_categ)
    return render(request,"sitio/index.html", {
        "lista_productos": queryset,
        "lista_categorias": Categoria.objects.all(),
        "categoria_seleccionada": una_categ
    })
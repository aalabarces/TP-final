from django import forms
from django.forms import widgets
from .models import Producto, Categoria

class FormProducto(forms.ModelForm):

    #campos del modelo
    class Meta:
        model = Producto
        fields = ('categoria', 'nombre', 'precio', 'descripcion', 'imagen')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'pub_nombre'}),
            'precio': forms.NumberInput(attrs={'class': 'pub_precio'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'pub_imagen'}),
            'descripcion': forms.TextInput(attrs={'class': 'pub_descripcion'}),
            #'fecha_publicacion': forms.SelectDateWidget(attrs={'class': 'pub_fecha_publicacion'}),
        }

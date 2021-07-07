from django.urls import path, include
from . import views

app_name = "carrito"
urlpatterns = [
    path('', views.carrito, name="carrito"),
    path('agregar/<int:producto_id>', views.agregar, name="agregar"),
    path('quitar/<int:producto_id>', views.quitar, name="quitar"),
    path('eliminar/<int:producto_id>', views.eliminar, name="eliminar"),
    path('limpiar/', views.limpiar, name="limpiar")
]
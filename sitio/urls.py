from django.urls import path, include
from . import views

app_name = "sitio"
urlpatterns = [
    path('', views.index, name="index"),
    path('registro', views.registro, name="registro"),
    path('filtro_categorias/<int:categ_id>', views.filtro_categorias, name="filtro_categorias"),
    path('<int:producto_id>', views.producto, name="producto"),
    path('producto_editar/<int:producto_id>', views.producto_editar, name="producto_editar"),
    path('producto_eliminar/<int:producto_id>', views.producto_eliminar, name="producto_eliminar"),
    path('producto_nuevo', views.producto_nuevo, name="producto_nuevo"),
    path('acercade', views.acercade, name="acercade"),
    path('contacto/', views.contacto, name="contacto")
]
from django.contrib import admin
from .models import Producto, Categoria, Etiqueta, DetalleProducto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(DetalleProducto)
class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'dimensiones', 'peso']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria']
    list_filter = ['categoria', 'etiquetas']
    search_fields = ['nombre']
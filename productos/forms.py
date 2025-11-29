from django import forms
from .models import Producto, Categoria, Etiqueta, DetalleProducto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']


class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['dimensiones', 'peso']


class ProductoForm(forms.ModelForm):
    etiquetas = forms.ModelMultipleChoiceField(
        queryset=Etiqueta.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
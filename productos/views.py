from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Etiqueta, DetalleProducto
from .forms import ProductoForm, CategoriaForm, EtiquetaForm


# ===== VISTAS ÍNDICE =====
def index(request):
    return render(request, 'index.html')


# ===== VISTAS PRODUCTOS =====
def lista_productos(request):
    # Obtener parámetro de búsqueda si existe
    nombre = request.GET.get('nombre', '')
    categoria_id = request.GET.get('categoria', '')
    
    productos = Producto.objects.all()
    
    if nombre:
        productos = productos.filter(nombre__icontains=nombre)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    categorias = Categoria.objects.all()
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'nombre_busqueda': nombre,
    }
    return render(request, 'productos/lista.html', context)


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            
            # Obtener datos de detalles si vienen en POST
            dimensiones = request.POST.get('dimensiones', '')
            peso = request.POST.get('peso', '')
            
            if dimensiones or peso:
                DetalleProducto.objects.create(
                    producto=producto,
                    dimensiones=dimensiones,
                    peso=peso if peso else None
                )
            
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'productos/crear.html', {'form': form})


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle.html', {'producto': producto})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            
            # Actualizar detalles
            dimensiones = request.POST.get('dimensiones', '')
            peso = request.POST.get('peso', '')
            
            detalle, _ = DetalleProducto.objects.get_or_create(producto=producto)
            detalle.dimensiones = dimensiones
            detalle.peso = peso if peso else None
            detalle.save()
            
            return redirect('detalle_producto', id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    
    context = {
        'form': form,
        'producto': producto,
    }
    return render(request, 'productos/editar.html', context)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    
    return render(request, 'productos/eliminar.html', {'producto': producto})


# ===== VISTAS CATEGORÍAS =====
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    
    return render(request, 'categorias/formulario.html', {'form': form, 'accion': 'Crear'})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categorias/formulario.html', {'form': form, 'accion': 'Editar'})


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    
    return render(request, 'categorias/formulario.html', {'categoria': categoria})


# ===== VISTAS ETIQUETAS =====
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas/lista.html', {'etiquetas': etiquetas})


def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    
    return render(request, 'etiquetas/formulario.html', {'form': form, 'accion': 'Crear'})


def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    
    return render(request, 'etiquetas/formulario.html', {'form': form, 'accion': 'Editar'})


def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    
    return render(request, 'etiquetas/formulario.html', {'etiqueta': etiqueta})
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class DetalleProducto(models.Model):
    # Relación Uno a Uno
    producto = models.OneToOneField('Producto', on_delete=models.CASCADE, related_name='detalle')
    dimensiones = models.CharField(max_length=100, blank=True)
    peso = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Relación Muchos a Uno
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    
    # Relación Muchos a Muchos
    etiquetas = models.ManyToManyField(Etiqueta, related_name='productos')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-id']
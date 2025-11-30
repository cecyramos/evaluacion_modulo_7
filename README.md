# Gestor de Productos Django

Sistema web para gestionar productos, categorías y etiquetas con operaciones CRUD completas. Proyecto desarrollado con Django y PostgreSQL.

## 📋 Características Implementadas

### Base de Datos
- ✅ Conexión a PostgreSQL
- ✅ Migraciones correctamente gestionadas

### Modelos
- ✅ **Producto**: nombre, descripción, precio
- ✅ **Categoría**: nombre, descripción
- ✅ **Etiqueta**: nombre
- ✅ **DetalleProducto**: dimensiones, peso

### Relaciones
- ✅ **Muchos a Uno**: Producto → Categoría (un producto pertenece a una categoría)
- ✅ **Muchos a Muchos**: Producto ↔ Etiqueta (productos pueden tener múltiples etiquetas)
- ✅ **Uno a Uno**: Producto → DetalleProducto (cada producto tiene detalles únicos)

### Funcionalidades
- ✅ CRUD completo para Productos, Categorías y Etiquetas
- ✅ Filtrado de productos por nombre y categoría
- ✅ Panel administrativo de Django
- ✅ Protección CSRF en formularios
- ✅ Interfaz Bootstrap responsive

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- PostgreSQL instalado y corriendo
- pip (gestor de paquetes de Python)

### Paso 1: Clonar el repositorio
```bash
cd producto_app
```

### Paso 2: Crear entorno virtual
```bash
python -m venv myenv
```

### Paso 3: Activar entorno virtual

**Windows:**
```bash
myenv\Scripts\activate
```

**Mac/Linux:**
```bash
source myenv/bin/activate
```

### Paso 4: Instalar dependencias
```bash
pip install django
pip install psycopg2
```

### Paso 5: Crear base de datos en PostgreSQL

Abre PgAdmin y create la base de datos:

```sql
CREATE DATABASE producto_db;
```

### Paso 6: Configurar base de datos

Edita `config/settings.py` y actualiza la configuración de la base de datos:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'producto_db',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Paso 7: Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 8: Crear superusuario
```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

### Paso 9: Ejecutar servidor
```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 📁 Estructura del Proyecto

```
producto_app/
├── config/
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # URLs principales
│   └── wsgi.py
├── productos/
│   ├── models.py            # Modelos de datos
│   ├── views.py             # Vistas (lógica CRUD)
│   ├── forms.py             # Formularios
│   ├── urls.py              # URLs de la app
│   ├── admin.py             # Configuración del admin
│   └── migrations/          # Migraciones de BD
├── templates/
│   ├── base.html            # Template base
│   ├── index.html           # Página principal
│   ├── productos/
│   │   ├── lista.html
│   │   ├── crear.html
│   │   ├── detalle.html
│   │   ├── editar.html
│   │   └── eliminar.html
│   ├── categorias/
│   │   ├── lista.html
│   │   └── formulario.html
│   └── etiquetas/
│       ├── lista.html
│       └── formulario.html
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## 🌐 Rutas Disponibles

### Página Principal
- `http://127.0.0.1:8000/` - Página de inicio

### Productos
- `/productos/` - Lista de productos (con filtros)
- `/productos/crear/` - Crear nuevo producto
- `/productos/<id>/` - Ver detalle de producto
- `/productos/<id>/editar/` - Editar producto
- `/productos/<id>/eliminar/` - Eliminar producto

### Categorías
- `/categorias/` - Lista de categorías
- `/categorias/crear/` - Crear categoría
- `/categorias/<id>/editar/` - Editar categoría
- `/categorias/<id>/eliminar/` - Eliminar categoría

### Etiquetas
- `/etiquetas/` - Lista de etiquetas
- `/etiquetas/crear/` - Crear etiqueta
- `/etiquetas/<id>/editar/` - Editar etiqueta
- `/etiquetas/<id>/eliminar/` - Eliminar etiqueta

### Panel Administrativo
- `/admin/` - Panel de administración de Django

## 💻 Uso del Sistema

### 1. Crear Categorías
Primero crea categorías desde `/categorias/crear/` o desde el admin.

### 2. Crear Etiquetas (Opcional)
Crea etiquetas desde `/etiquetas/crear/`.

### 3. Crear Productos
Ve a `/productos/crear/` y completa el formulario:
- Nombre del producto
- Descripción
- Precio
- Categoría (selecciona una existente)
- Etiquetas (opcional, múltiples)
- Dimensiones (opcional)
- Peso (opcional)

### 4. Gestionar Productos
- **Ver lista**: `/productos/`
- **Filtrar**: Usa el formulario de búsqueda por nombre o categoría
- **Ver detalles**: Click en "Ver" en cualquier producto
- **Editar**: Click en "Editar"
- **Eliminar**: Click en "Eliminar" y confirma

## 🔧 Consultas ORM Implementadas

El sistema implementa las siguientes consultas con el ORM de Django:

```python
# Filtrado por nombre (insensible a mayúsculas)
productos = Producto.objects.filter(nombre__icontains=nombre)

# Filtrado por categoría
productos = Producto.objects.filter(categoria_id=categoria_id)

# Obtener productos con sus relaciones
producto = Producto.objects.get(id=id)
producto.categoria.nombre
producto.etiquetas.all()
producto.detalle.dimensiones
```

## 🔐 Seguridad

El proyecto implementa las siguientes medidas de seguridad:

- ✅ Protección CSRF en todos los formularios (`{% csrf_token %}`)
- ✅ Middleware de seguridad de Django habilitado
- ✅ Validación de formularios del lado del servidor
- ✅ Uso de ORM para prevenir SQL injection

## 🎨 Interfaz

- Bootstrap 5 para diseño responsive
- Templates que heredan de `base.html`
- Formularios Django estándar con `form.as_p`
- Navbar con navegación principal

## ⚙️ Panel Administrativo

Accede al panel en `/admin/` con el superusuario creado.

Desde el admin puedes:
- Gestionar productos, categorías y etiquetas
- Ver relaciones entre modelos
- Realizar búsquedas y filtros avanzados

## 🐛 Solución de Problemas

### Error de conexión a PostgreSQL
- Verifica que PostgreSQL esté corriendo
- Confirma usuario, contraseña y puerto en `settings.py`
- Asegúrate de que la base de datos `producto_db` existe

### Error "No module named 'psycopg2'"
```bash
pip install psycopg2-binary
```

### Error "TemplateDoesNotExist"
- Verifica que la carpeta `templates/` esté en la raíz del proyecto
- Confirma que `TEMPLATES` en `settings.py` tenga: `'DIRS': [BASE_DIR / 'templates']`

### Error "No such table"
```bash
python manage.py migrate
```

## 📝 Notas Adicionales

- `DEBUG = True` está habilitado para desarrollo. Cambiar a `False` en producción.
- Los datos sensibles (contraseñas, SECRET_KEY) deberían estar en variables de entorno en producción.
- El proyecto usa SQLite por defecto hasta que se configure PostgreSQL.

## 📄 Licencia

Este proyecto es de código abierto bajo la licencia MIT - Cecilia Ramos Alcatruz

---

**Desarrollado con Django 5.2.8 y PostgreSQL**
#  BookSpace

**BookSpace** es una aplicación web de gestión de librería desarrollada con Django. Permite administrar productos (libros), clientes, ventas y usuarios con diferentes roles.

---

## Tecnologías utilizadas

- **Python 3.x**
- **Django 5.2.5**
- **SQLite3** (base de datos)
- **HTML/CSS** (templates)

---

## Funcionalidades

- **Gestión de usuarios** con roles: Admin, Empleado y Cliente
- **Catálogo de productos** con nombre, descripción, precio, stock, imagen y PDF
- **Registro de clientes** con nombre, email y teléfono
- **Módulo de ventas** con detalle por producto y cantidad
- **Formulario de contacto**
- Panel de administración de Django

---

##  Estructura del proyecto

```
bookspace/
├── bookspace/              # Configuración principal de Django
├── bookspace_app/          # Aplicación principal
│   ├── migrations/         # Migraciones de base de datos
│   ├── scripts/            # Scripts utilitarios
│   ├── static/             # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/          # Plantillas HTML
│   ├── models.py           # Modelos: Usuario, Producto, Cliente, Venta
│   ├── views.py            # Vistas y lógica de negocio
│   ├── urls.py             # Rutas de la aplicación
│   └── admin.py            # Configuración del panel admin
├── db.sqlite3              # Base de datos SQLite
├── manage.py               # Script de gestión de Django
└── requirements.txt        # Dependencias del proyecto
```

---

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/norah30/bookspace.git
cd bookspace
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre tu navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Modelos de base de datos

| Modelo | Descripción |
|---|---|
| `Usuario` | Usuarios del sistema con roles (admin, empleado, cliente) |
| `Producto` | Libros con precio, stock, imagen y PDF |
| `Cliente` | Clientes registrados de la tienda |
| `Venta` | Registro de ventas asociadas a usuario y cliente |
| `DetalleVenta` | Detalle de productos por venta |
| `Contacto` | Mensajes del formulario de contacto |

---

## Autor

Desarrollado por [@norah30](https://github.com/norah30)

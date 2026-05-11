# BookSpace

**BookSpace** es una aplicación web para una librería en línea, desarrollada con Django. Permite explorar el catálogo de libros, gestionar ventas, recibir mensajes de contacto y consultar el clima en tiempo real mediante integración con APIs externas.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-green?logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-33%25-orange?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-27%25-blue?logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/Base%20de%20datos-SQLite3-lightblue?logo=sqlite&logoColor=white)

---

## Funcionalidades

-  Página de inicio con presentación de la librería
-  Catálogo de productos (libros) con precios e imágenes
-  Sección de oferta del mes
-  Localización de la tienda
-  Sección de noticias
-  Consulta del clima en tiempo real (API OpenWeatherMap)
-  Formulario de contacto con guardado en base de datos y envío por FTP
-  Sistema de login con roles: Administrador, Empleado y Cliente
-  Módulo de ventas con registro de clientes y detalle de venta

---

##  Tecnologías utilizadas

| Capa | Tecnología |
|------|------------|
| Backend | Python 3, Django 5.2 |
| Frontend | HTML, CSS, JavaScript |
| Base de datos | SQLite3 |
| API externa | OpenWeatherMap API |
| Transferencia | FTP (script automatizado) |
| Dependencias HTTP | `requests` |

---

## Estructura del proyecto
bookspace/
├── bookspace/ # Configuración principal de Django
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── bookspace_app/ # Aplicación principal
│ ├── models.py # Modelos: Usuario, Producto, Cliente, Venta, Contacto
│ ├── views.py # Vistas y lógica de negocio
│ ├── urls.py # Rutas de la aplicación
│ ├── templates/ # Plantillas HTML
│ ├── static/ # Archivos estáticos (CSS, imágenes)
│ ├── scripts/ # Script FTP para envío de datos
│ └── migrations/ # Migraciones de base de datos
├── db.sqlite3 # Base de datos SQLite
├── manage.py # Gestor de Django
└── requirements.txt # Dependencias del proyecto


---

##  Instalación y configuración

### Requisitos previos

- Python 3.10+
- pip
- Cuenta en [OpenWeatherMap](https://openweathermap.org/api) para obtener una API Key

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/norah30/bookspace.git
cd bookspace

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar la API Key del clima
# En bookspace/settings.py agrega:
# OWM_API_KEY = "tu_api_key_aquí"

# 5. Aplicar migraciones
python manage.py migrate

# 6. Iniciar el servidor
python manage.py runserver
```

Abre tu navegador en `http://127.0.0.1:8000`

---

##  Integración con OpenWeatherMap

La vista `/clima` consulta la API de OpenWeatherMap para mostrar temperatura, humedad, descripción del clima y velocidad del viento de cualquier ciudad ingresada por el usuario.

```python
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
```

---

##  Modelos de datos

| Modelo | Descripción |
|--------|-------------|
| `Usuario` | Gestión de usuarios con roles (Admin, Empleado, Cliente) |
| `Producto` | Catálogo de libros con precio, stock, imagen y PDF |
| `Cliente` | Registro de clientes con nombre, email y teléfono |
| `Venta` | Registro de ventas asociadas a usuario y cliente |
| `DetalleVenta` | Detalle de productos por venta con cantidad y precio |
| `Contacto` | Mensajes recibidos desde el formulario de contacto |

---

##  Dependencias
Django==5.2
requests==2.32.5
asgiref==3.9.1
sqlparse==0.5.3


---

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---

> Desarrollado con 💙 usando Django




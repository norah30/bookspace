from django.db import models

# Create your models here.

# Tabla: usuarios
class Usuario(models.Model):
    ROLES = [
        ('admin', 'Admin'),
        ('empleado', 'Empleado'),
        ('cliente', 'Cliente'),
    ]
    usu_nombre = models.CharField(max_length=100)
    usu_email = models.EmailField(unique=True)
    usu_password = models.CharField(max_length=255)
    usu_rol = models.CharField(max_length=10, choices=ROLES, default='empleado')

    def __str__(self):
        return self.usu_nombre


# Tabla: productos
class Producto(models.Model):
    pro_nombre = models.CharField(max_length=100)
    pro_descripcion = models.TextField(blank=True, null=True)
    pro_precio = models.DecimalField(max_digits=10, decimal_places=2)
    pro_stock = models.IntegerField()
    pro_imagen = models.CharField(max_length=255, blank=True, null=True)
    pro_pdf = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.pro_nombre


# Tabla: clientes
class Cliente(models.Model):
    cli_nombre = models.CharField(max_length=100)
    cli_email = models.EmailField(blank=True, null=True)
    cli_telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.cli_nombre


# Tabla: ventas
class Venta(models.Model):
    ven_fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Venta {self.id} - {self.ven_fecha}"


# Tabla: detalles_venta
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    det_cantidad = models.IntegerField()
    det_precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id} - Venta {self.venta.id}"


# Tabla: contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre}"

from django.db import models

# Create your models here.

class registros_usuarios(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45, verbose_name='Nombres' )
    apellidos=models.CharField( max_length=60, verbose_name='Apellidos' )
    correo_electronico=models.CharField( max_length=45, verbose_name='Correo')
    password=models.CharField( max_length=12, verbose_name='Contraseña')
    
def __str__(self):
    fila = "Nombres: " + self.nombre + " - " + "Apellidos: " + self.apellidos + " - " + "Correo: " + self.correo_electronico + " - " "Contraseña: " + self.password
    return fila 

def delete(self, using=None, keep_parents=False):
    self.nombre.delete(self.nombre)
    super().delete()

class roles(models.Model):
    id_rol=models.AutoField(primary_key=True)
    rol=models.CharField(max_length=20, verbose_name='Rol')

def __str__(self):
    filaR = "Rol: " + self.rol
    return filaR

def delete(self, using=None, keep_parents=False):
    self.rol.delete(self.rol)
    super().delete()

class Login(models.Model):
    user = models.CharField(max_length=255, verbose_name='Correo Electronico')
    password = models.CharField(max_length=255, verbose_name='password')

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=50)

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, verbose_name='ItemCarrito')

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Venta(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
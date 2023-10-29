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
#-----------------------------------------------------------------------------------------------------
class roles(models.Model):
    id_rol=models.AutoField(primary_key=True)
    rol=models.CharField(max_length=20, verbose_name='Rol')

def __str__(self):
    filaR = "Rol: " + self.rol
    return filaR

def delete(self, using=None, keep_parents=False):
    self.rol.delete(self.rol)
    super().delete()
#-----------------------------------------------------------------------------------------------------
class Login(models.Model):
    user = models.CharField(max_length=255, verbose_name='Correo Electronico')
    password = models.CharField(max_length=255, verbose_name='password')
#-----------------------------------------------------------------------------------------------------
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100, verbose_name='Categoria')
#----------------------------------------------------------------------------------------------------
class Productos(models.Model):
    id_producto=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    descripcion = models.CharField(max_length=50, verbose_name='Descripcion')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    imagen = models.ImageField(upload_to='images/',verbose_name='imagen', null=True)
    cantidad = models.PositiveIntegerField(verbose_name='cantidad')
    categoria =models.ForeignKey("Categoria", verbose_name='categoria', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True,verbose_name='aviable')
#-----------------------------------------------------------------------------------------------------
class Carrito(models.Model):
    id_carrito=models.AutoField(primary_key=True)
    producto = models.ForeignKey("Productos", verbose_name='producto', on_delete=models.CASCADE)
#-----------------------------------------------------------------------------------------------------
class ItemCarrito(models.Model):
    carrito = models.ForeignKey("Carrito", verbose_name='carrito', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
#-----------------------------------------------------------------------------------------------------
class PedidoRealizado(models.Model):
    id_pedido =models.AutoField(primary_key=True)
    carrito = models.ForeignKey('Carrito',verbose_name='productos',on_delete=models.CASCADE)
#-----------------------------------------------------------------------------------------------------
class Venta(models.Model):
    carrito = models.ForeignKey("Carrito", verbose_name='carrito', on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
#-----------------------------------------------------------------------------------------------------

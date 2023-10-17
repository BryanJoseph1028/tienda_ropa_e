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

class roles(models.Model):
    id_rol=models.AutoField(primary_key=True)
    rol=models.CharField(max_length=20, verbose_name='Rol' )

def __str__(self):
    filaR = "Rol: " + self.rol
    return filaR


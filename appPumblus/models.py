from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


CANTIDAD_CHUMBLES = [
    ("KC°", "KC°"),
    ("%Z", "%Z"),
    ("O", "O"),
    ("O)", "O)"),
]
# Create your models here.
# Usuario, el cliente 
class Usuario(AbstractUser):
    rut = models.CharField(max_length=12)
    groups = models.ManyToManyField(Group, related_name='custom_user')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    
#Colocamos los pumblus que es lo segundo más importante


class PumblusX(models.Model):
    idProducto=models.IntegerField(primary_key=True, null=False, error_messages="Debe ingresar un producto")
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    largo_dingle_dop = models.DecimalField(max_digits=5, decimal_places=2)
    vibracion_floops = models.IntegerField()
    grodus_inalambrico = models.BooleanField()
    imagen= models.ImageField(upload_to='notenemosfotoytengosueño') 


class Pumblus (models.Model):
    idProducto=models.IntegerField(primary_key=True, null=False, error_messages="Debe ingresar un producto")
    nombre=models.CharField(max_length=50, null=False)
    precio= models.IntegerField(null=False)
    f_creacion=models.DateField()
    f_caducidad=models.DateField()
    c_chumbles=models.CharField(choices=CANTIDAD_CHUMBLES, max_length=10)
    imagen= models.ImageField(upload_to='notenemosfotoytengosueño')  
    
#Carrito y productoss


class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pumblus = models.ForeignKey(Pumblus, on_delete=models.CASCADE )
    pumblusX = models.ForeignKey(PumblusX, on_delete=models.CASCADE, null=True)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.pumblus.precio * self.cantidad #despues arreglamos esto

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    carrito = models.ManyToManyField(Carrito)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=100, default='Pendiente')
    direccion_envio = models.CharField(max_length=150)


#El Staff lo puse que usara los datos del usuario
class Staff(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nick = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    imagenPerfil = models.ImageField(upload_to='notenemosfotoytengosueño')



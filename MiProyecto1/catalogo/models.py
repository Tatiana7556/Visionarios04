from django.db import models

# Create your models here.
class compra(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombres', null=True)
    direccion=models.CharField(max_length=100, verbose_name='Direccion', null=True)
    telefono=models.CharField(max_length=15, null=True, verbose_name='Telefono')
    correo=models.EmailField(unique=True,verbose_name='Correo Electronico', null=True)
    pago=models.CharField(
        max_length=25,
        null=False, blank=False,
        default='Pago contra Entrega'
        ,verbose_name=' Medio De Pago'
    )
    mensaje=models.TextField(null=True)

 



class catalogo(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')

    def __str__(self):
        return self.nombre

class LG(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')

class mabe (models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')

class challenger(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')

class abba (models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')

class whirlpool(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')

class televisores(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')

class electrodomesticos(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')

class sonido(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    precio= models.FloatField()
    imagen=models.ImageField(upload_to='image')    
    



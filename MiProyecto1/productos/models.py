from django.db import models

# Create your models here.

class producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, verbose_name="Nombre")
    marca=models.CharField(max_length=40, verbose_name="Marca")
    descripcion=models.TextField(verbose_name="Descripcion" , null=True)
    cantidad=models.PositiveIntegerField(verbose_name="Cantidad", null=True)
    precio=models.FloatField(verbose_name="Precio")
    imagen=models.ImageField(upload_to='imagenes/',verbose_name="Imagen" , null=True)
    
    def __str__(self):
        fila="Nombre:" + self.nombre + "-" + "Marca:" + self.marca + "-" +"Descripcion:" + self.descripcion 
        return fila

    def delete(self, using=None , keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


from django.db import models

# Create your models here.

class usuario (models.Model):
    id=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length= 15, blank= False, null= False)
    apellidos=models.CharField(max_length= 15, blank= False, null= False)
    correo= models.CharField(max_length= 50, blank= False, null= False)
    contraseña= models.CharField(max_length= 20, blank= False, null= False)
    

    def __str__(self):
        fila="Nombres:" + self.nombres + "-" + "Apellidos:" + self.apellidos + "-" +"Correo:" + self.correo
        return fila
 


    
from django.db import models

# Create your models here.

class DatosPersona(models.Model):
    Nombre = models.CharField(max_length=35)
    Direccion = models.CharField(max_length=40)
    Telefono = models.IntegerField()
    Mail = models.EmailField()
    Asunto = models.CharField(max_length=20)
    Mensaje = models.CharField(max_length=200)

    
    def Datos(self):
        cadena = "{0}, {1}, {2}, {3}"
        return cadena.format(self.Nombre, self.Direccion, self.Telefono, self.Mail)

    def __str__(self):
        return self.Datos()

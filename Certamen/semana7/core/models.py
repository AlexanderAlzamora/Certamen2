from django.db import models
from django.contrib.auth.models import User


    
#Seleccionar el Tema sobre el cual quiere realizar su proyecto
tipo_mensajes=[
    ("Futbol","Futbol"),
    ("Software","Software"),
    ("Investigacion","Investigacion"),
]
    

class Mensaje(models.Model):
    Nombree= models.CharField(max_length=50)#Nombre del proyecto pensado
    tipo= models.CharField(max_length=50,choices=tipo_mensajes)#escoger las opciones de arriba
    alumno= models.CharField(max_length=50)#nombres de los alumnos/alumno
    profesor=models.CharField(max_length=50)#Se crea para que despues un profesor pueda ingresar su nombre en el proyecto enviado por el alumno
    informacion=models.CharField(max_length=300) #Ideas sobre su proyecto
    def __str__(self) -> str:
        return self.tipo
    
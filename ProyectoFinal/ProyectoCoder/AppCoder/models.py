from email.quoprimime import body_check
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User




class Socios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    actividad=models.CharField(max_length=50)
        
    def __str__(self):

        return f"nombre: {self.nombre} - apellido{self.apellido} - email {self.email} - actividad {self.actividad}"


class Instalaciones(models.Model):
    imagen=models.ImageField(upload_to='instalaciones', null=True, blank=True)


class Nosotros(models.Model):
    imagen=models.ImageField(upload_to='nosotros', null=True, blank=True)

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='agragarAvatar', null=True, blank=True)



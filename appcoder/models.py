from django.db import models
from django.contrib.auth.models import User

# create your models here
class Proyectos_Ley(models.Model):

    nombre= models.CharField(max_length=40)
    tematica=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.tematica}"

class Integrantes_proyect(models.Model):
    nombre= models.CharField(max_length=40)
    apellido=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"

class Camara(models.Model):
    nombre=models.CharField(max_length=40)
    integrantes=models.IntegerField(max_length=20)
    profesion=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} - {self.integrantes} - {self.profesion}"

class Fecha_Inicio(models.Model):
    fecha= models.DateField(max_length=20)

    def __str__(self):
        return f"{self.fecha}"

# clase 24
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

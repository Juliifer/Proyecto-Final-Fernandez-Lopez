from django.db import models

# create your models here
class Proyectos_Ley(models.Model):

    nombre= models.CharField(max_length=40)
    tematica=models.IntegerField()

class Integrantes_proyect(models.Model):
    nombre= models.CharField(max_length=40)
    apellido=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)

class Camara(models.Model):
    nombre=models.CharField(max_length=40)
    cantidad_miembros=models.CharField(max_length=20)
    profesion=models.CharField(max_length=30)

class Fecha_Inicio(models.Model):
    fecha= models.DateField(max_length=20)
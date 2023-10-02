from django.db import models

# create your models here
class Proyectos_Ley(models.Model):

    nombre= models.CharField()
    tematica=models.IntegerField()

class Integrantes_proyect(models.Model):
    nombre= models.CharField()
    apellido=models.CharField()
    email=models.EmailField()

class Camara(models.Model):
    nombre=models.CharField()
    cantidad_miembros=models.CharField()
    profesion=models.CharField()

class Fecha_Inicio(models.Model):
    fecha= models.CharField()
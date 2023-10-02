from django.db import models

# create your models here
class Proyectos_Ley(models.Model):

    nombre= models.CharField(max_lenght=20)
    tematica=models.IntegerField(max_length=40)

class Integrantes_proyect(models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_lenght=30)
    email=models.EmailField()

class Camara(models.Model):
    nombre=models.CharField(max_length=30)
    cantidad_miembros=models.CharField()
    profesion=models.CharField(max_length=30)

class Fecha_Inicio(models.Model):
    fecha= models.CharField()
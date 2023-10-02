from django.db import models

# create your models here
class Curso(models.Model):

    curso = models.CharField(max_lenght=20)
    camada=models.IntegerField()

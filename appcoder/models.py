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
    email=models.EmailField(max_length=40, blank= True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"

class Camara(models.Model):
    nombre=models.CharField(max_length=40)
    integrantes=models.CharField(max_length=20)
    profesion=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} - {self.integrantes} - {self.profesion}"

    
from django.conf import settings


class Avatar(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imagen = models.ImageField(
        upload_to='avatars/', default='avatars/default.png')
   

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')  # Campo para la imagen, se almacenará en la carpeta 'blog_images/'

    def __str__(self):
        return self.title
    
    

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



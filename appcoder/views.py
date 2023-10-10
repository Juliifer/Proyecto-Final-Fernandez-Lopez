from django.shortcuts import render
from appcoder.models import Proyecto

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def Proyectos_Ley(request):
    return render(request, 'AppCoder/Proyectos_Ley.html')

def Integrantes_proyect(request):
    return render(request, 'AppCoder/Integrantes_proyect.html')

def Camara(request):
    return render(request, 'AppCoder/camara.html')

def Fecha_Inicio(request):
    return render(request, 'AppCoder/fecha_inicio.html')

def cursoFormulario(request):
    return render(request, 'AppCoder/cursoFormulario.html')

def cursoFormulario(request):
    if request.method == 'POST':

        curso = Proyecto (request.POST['nombre'], request.POST['rubro'])

        curso.save()

        return render(request, 'AppCoder/inicio.html')
    return render (request, 'AppCoder/cursoFormulario.html')
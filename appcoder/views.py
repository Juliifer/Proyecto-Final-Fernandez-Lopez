from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def Proyectos_Ley(request):
    return render(request, 'AppCoder/Proyectos._Ley.html')

def Integrantes_proyect(request):
    return render(request, 'AppCoder/Integrantes_proyect.html')

def Camara(request):
    return render(request, 'AppCoder/camara.html')

def Fecha_Inicio(request):
    return render(request, 'AppCoder/fecha_inicio.html')


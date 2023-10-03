from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppCoder/index.html')

def Proyectos_Ley(request):
    return render(request, 'AppCoder/proyectos_ley.html')

def Integrantes_proyect(request):
    return render(request, 'AppCoder/integrantes.html')

def Camara(request):
    return render(request, 'AppCoder/camara.html')

def Fecha_Inicio(request):
    return render(request, 'AppCoder/fecha_inicio.html')


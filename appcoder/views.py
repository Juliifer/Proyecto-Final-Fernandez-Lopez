from django.shortcuts import render

def inicio(request):
    return render (request, 'AppCoder/inicio.html')

def Proyectos_Ley(request):
    return render(request, 'AppCoder/proyectos_ley.html')

def Integrantes_proyect(request):
    return render(request, 'AppCoder/integrantes.html')

def Camara(request):
    return render(request, 'AppCoder/camara.html')

def Fecha_Inicio(request):
    return render (request, 'AppCoder/fecha_inicio.html')


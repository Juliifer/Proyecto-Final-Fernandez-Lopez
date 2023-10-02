from django.http import HttpResponse

def inicio(request):
    return HttpResponse('vista inicio')

def Proyectos_Ley(request):
    return HttpResponse('vista proyectos de ley')

def Integrantes_proyect(request):
    return HttpResponse ('vista integrantes del proyecto')

def Camara(request):
    return HttpResponse ('vista camara o secretaria')

def Fecha_Inicio(request):
    return HttpResponse ('vista fecha inicio proyecto')


from django.shortcuts import render
from appcoder.forms import CursoFormulario
from appcoder.models import Proyectos_Ley

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

        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data

                proyecto = Proyectos_Ley (nombre=informacion['nombre'], rubro=informacion['rubro'])

                proyecto.save()

                return render(request, 'AppCoder/inicio.html')
        
    else:

        miFormulario = CursoFormulario() 

    return render(request, 'AppCoder/cursoFormulario.html', {'miFormulario': miFormulario})
from django.shortcuts import render
from appcoder.models import Proyectos_Ley, Integrantes_proyect, Camara
from appcoder.forms import cursoFormulario, BuscaCursoForm
def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def proyectos_Ley(request):
    return render(request, 'AppCoder/Proyectos_Ley.html')

def integrantes_proyect(request):
    return render(request, 'AppCoder/Integrantes_proyect.html')

def camara(request):
    return render(request, 'AppCoder/camara.html')

def Fecha_Inicio(request):
    return render(request, 'AppCoder/fecha_inicio.html')

def CursoFormulario(request):
    if request.method == 'POST':
        
        proyecto = Proyectos_Ley (nombre=request.POST['nombre'], tematica=request.POST['tematica'])

        proyecto.save()

        return render (request, 'AppCoder/inicio.html')
    
    return render(request, 'AppCoder/cursoFormulario.html')

def integrantesFormulario(request):
    if request.method == 'POST':
        
        integrantes = Integrantes_proyect (nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])

        integrantes.save()

        return render (request, 'AppCoder/inicio.html')
    
    return render(request, 'AppCoder/integrantesFormulario.html')

def camaraFormulario(request):
    if request.method == 'POST':
        
        camara = Camara (nombre=request.POST['nombre'], integrantes=request.POST['integrantes'], profesion=request.POST['profesion'])

        camara.save()

        return render (request, 'AppCoder/inicio.html')
    
    return render(request, 'AppCoder/camaraFormulario.html')

def busqueda_proyecto_ley_form(request):
    return render(request, 'AppCoder/busqueda_proyecto_ley.html')


def busqueda_proyecto_ley(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre", "")
        proyectos_ley = Proyectos_Ley.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppCoder/resultados_busqueda.html', {'proyectos_ley': proyectos_ley})

def leerProyectos(request):
    proyectos = Proyectos_Ley.objects.all() #trae todos los proyectos
    return render(request, "AppCoder/leerProyectos.html", {'proyectos': proyectos})

def delete_proyecto(request, proyecto_id):
    print('\n\n\n\n')
    print(type(proyecto_id))

    proyectos = Proyectos_Ley.objects.get(id=int(proyecto_id))
    proyectos.delete()

    return render(request, "AppCoder/leerProyectos.html", {"proyecto": proyectos})

def edit_proyecto(request, proyecto_id):

    if request.method == 'POST':
        miFormulario = cursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
           
            proyecto= Proyectos_Ley.objects.get(id=proyecto_id)
            proyecto.nombre = informacion['proyecto']
            proyecto.tematica = informacion['tematica']
            proyecto.save()

            return render(request, "AppCoder/inicio.html")
        
    else: 
        proyecto = Proyectos_Ley.objects.get(id=proyecto_id)
        miFormulario = cursoFormulario(initial={'proyecto':proyecto.nombre})

    return render(request, "AppCoder/create_api_form.html", {'miFormulario':miFormulario})

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class IntegrantesList(ListView):
    model = Integrantes_proyect
    template_name= 'AppCoder/integrantes_list.html'

class IntegrantesDetalle(DetailView):
    model = Integrantes_proyect
    template_name= 'AppCoder/integrantes_detalle.html'

class IntegrantesCreacion(CreateView):
    model = Integrantes_proyect
    success_url = "/AppCoder/integrantes/list.html"
    fields = ['nombre', 'tematica']

class IntegrantesUpdate(UpdateView):
    model = Integrantes_proyect
    success_url = '/AppCoder/integrantes/list.html'
    fields = ['nombre', 'apellido', 'email']

class IntegrantesDelete(DeleteView):
    model = Integrantes_proyect
    success_url = '/AppCoder/integrantes/list'

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
   
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {'mensaje':f"Bienvenido {usuario}"})
            else:

                    return render(request, "AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"})
        
        else:

                return render (request, "AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {'form':form})
     
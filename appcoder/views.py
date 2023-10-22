from django.shortcuts import render, redirect
from appcoder.models import Proyectos_Ley, Integrantes_proyect, Camara
from appcoder.forms import cursoFormulario, BuscaCursoForm
from django.contrib.auth.decorators import login_required
from appcoder.models import Avatar
from django.contrib.auth import update_session_auth_hash


def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if avatares:
        avatar = avatares[0]
    else:
        avatar = None  # Otra acción que desees tomar si no hay imágenes
    
    return render(request, 'AppCoder/inicio.html', {"url": avatar })



def proyectos_Ley(request):
    return render(request, 'AppCoder/Proyectos_Ley.html')

@login_required
def integrantes_proyect(request):
    return render(request, 'AppCoder/Integrantes_proyect.html')

def camara(request):
    return render(request, 'AppCoder/camara.html')

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
from django.contrib.auth.mixins import LoginRequiredMixin

class IntegrantesList(ListView):
    model = Integrantes_proyect
    template_name= 'AppCoder/integrantes_list.html'

class IntegrantesDetalle(DetailView):
    model = Integrantes_proyect
    template_name= 'AppCoder/integrantes_detalle.html'

class IntegrantesCreacion(CreateView, LoginRequiredMixin):
    model = Integrantes_proyect
    success_url = "/AppCoder/integrantes/list.html"
    fields = ['nombre', 'apellido', "email"]

class IntegrantesUpdate(UpdateView):
    model = Integrantes_proyect
    success_url = '/AppCoder/integrantes/list.html'
    fields = ['nombre', 'apellido', 'email']

class IntegrantesDelete(DeleteView):
    model = Integrantes_proyect
    success_url = '/AppCoder/integrantes/list'

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from appcoder.forms import UserRegisterForm
from appcoder.forms import UserEditForm 


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        print(form)

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
     

def register(request):

    if request.method == 'POST':

           # form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST) 
        
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request, "AppCoder/inicio.html", {"mensaje":f"{username} Usuario Creado :)"})
        
    else:
        #form = UserCreationForm()
       form = UserRegisterForm() 
            
    return render(request, "AppCoder/signup.html", {"form":form})

@login_required
def edit(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            # Verifica si la contraseña está siendo modificada
            if informacion.get('password1'):
                if informacion['password1'] != informacion['password2']:
                    datos = {
                        'first_name': usuario.first_name,
                        'email': usuario.email
                    }
                    miFormulario = UserEditForm(initial=datos)
                else:
                    # Cambia la contraseña del usuario y guarda
                    usuario.set_password(informacion['password1'])
                    usuario.save()

                    # Actualiza la sesión del usuario sin cerrarla
                    update_session_auth_hash(request, usuario)

            # Actualiza otros campos del usuario
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            # Trata con la imagen del avatar (si aplica)
            try:
                avatar = Avatar.objects.get(user=usuario)
                # Actualiza la imagen si se proporciona en el formulario
                avatar.imagen = informacion.get('imagen', avatar.imagen)
                avatar.save()
            except Avatar.DoesNotExist:
                avatar = Avatar(user=usuario, imagen=informacion.get('imagen'))
                avatar.save()

            return render(request, 'AppCoder/inicio.html')
    else:
        datos = {
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "AppCoder/edit.html", {'miFormulario': miFormulario, 'usuario': usuario})


def about(request):
    return render(request, 'AppCoder/about.html')


from .models import Blog
from .forms import BlogForm 

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'AppCoder/blog_list.html', {'blogs': blogs})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'AppCoder/create_blog.html', {'form': form})

def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'AppCoder/edit_blog.html', {'form': form})


from django.shortcuts import render, get_object_or_404

def page_detail(request, page_id):
    page = get_object_or_404(Blog, pk=page_id)
    return render(request, 'AppCoder/page_detail.html', {'page': page})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import User
from .forms import UserProfileForm
@login_required
def view_profile(request):
    # Verifica si el usuario autenticado tiene un perfil asociado
    user = request.user  # Recupera el usuario autenticado

    # Puedes acceder a las propiedades del usuario, como username, email, etc.
    username = user.username
    email = user.email
    
    return render(request, 'AppCoder/profile.html', {'user': user, 'username': username, 'email': email})

@login_required
def delete_profile(request):
    user = request.user
    
    # Puedes agregar comprobaciones adicionales si es necesario
    
    # Eliminar el usuario y cerrar la sesión
    user.delete()
    logout(request)
    
    return redirect('Inicio')  # Redirige a la página de inicio u otra página de tu elección


from .models import Message
from .forms import MessageForm

@login_required
def message_list(request):
    user = request.user
    received_messages = Message.objects.filter(receiver=user)
    sent_messages = Message.objects.filter(sender=user)
    return render(request, 'messages/message_list.html', {
        'received_messages': received_messages,
        'sent_messages': sent_messages,
    })

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'AppCoder/send_message.html', {'form': form})
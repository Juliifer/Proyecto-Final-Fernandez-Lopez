from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login, authenticate
from users.forms import UserRegisterForm
from appcoder.forms import cursoFormulario, integrantesFormulario, UserRegisterForm, UserEditForm 

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
                return render(request, "AppCoder/inicio.html", {"mensaje":f"{username}Usuario Creado :)"})
        
    else:
        #form = UserCreationForm()
       form = UserRegisterForm() 
            
    return render(request, "AppCoder/register.html", {"form":form})
    

@login_required
def edit(request):
     usuario = request.user

     if request.method == 'POST':
          
          miFormulario = UserEditForm(request.POST)

          if miFormulario.is_valid():
               
               informacion = miFormulario.cleaned_data

               usuario.email = informacion['email']
               usuario.password1 = informacion['password1']
               usuario.password2 = informacion['password2']
               usuario.last_name = informacion['last_name']
               usuario.first_name = informacion['first_name']

               usuario.save()

               return render(request, 'AppCoder/inicio.html')
    
     else:
          miFormulario = UserEditForm(initial={'email':usuario.email})

     return render(request, "users/edit.html"), {'miFormulario':miFormulario, 'usuario':usuario}
 


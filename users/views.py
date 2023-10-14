from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login, authenticate
from users.forms import UserRegisterForm


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
    


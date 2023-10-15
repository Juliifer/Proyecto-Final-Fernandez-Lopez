from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión después del registro
            return redirect('perfil')  # Redirigir a la página de perfil
    else:
        form = RegistrationForm()
    return render(request, 'registro/registro.html', {'form': form})

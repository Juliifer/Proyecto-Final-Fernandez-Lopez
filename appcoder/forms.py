from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class cursoFormulario(forms.Form):
    proyecto = forms.CharField(max_length=20)
    tematica = forms.IntegerField()

class BuscaCursoForm(forms.Form):
    proyecto = forms.CharField()

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label='Ingrese su email:')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput, required=False)

    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model= User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

        help_texts = {k: "" for k in fields }


from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'author', 'image']
  


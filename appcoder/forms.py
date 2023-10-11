from django import forms

class CursoFormulario(forms.Form):

    #especificar los campos
    nombre = forms.CharField()
    rubro = forms.IntegerField()

class BuscaProyectoForm(forms.Form):
    proyecto = forms.CharField()
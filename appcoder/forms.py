from django import forms

class cursoFormulario(forms.Form):
    proyecto = forms.CharField(max_length=20)
    tematica = forms.IntegerField()

class BuscaCursoForm(forms.Form):
    proyecto = forms.CharField()
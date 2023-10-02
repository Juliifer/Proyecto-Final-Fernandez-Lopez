from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse ('Hola Django - Coder')

def segunda_vista(request):
    return HttpResponse('<br><br>Ya entendimos esto, es muy simple :)')

def miNombreEs(self, nombre):
    documentosDeTexto = f'Mi nombre es: <br><br>  {nombre}'

    return HttpResponse(documentosDeTexto)


def probando_template(request):
    nom = 'Nicolas'
    ap = 'Perez'

    diccionario = {
        'name': nom,
        'lastname':ap,
    }

    mihtml = open('./C:/Users/aleja/Documents/JULI/CLASE 17/Proyecto1/Proyecto1/plantillas/template.html')

    plantilla = Template(mihtml.read())

    mihtml.close()

    miContexto = Context(diccionario)

    midocumento = plantilla.render(miContexto)

    return HttpResponse(midocumento)

  

def probando_template2(request):
    nom = 'Ricardo'
    ap = 'Dominguez'
    listanotas = [3,7,8,9,2]

    diccionario = {
        'name': nom,
        'lastname':ap,
        'notas':listanotas
    }
    
    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
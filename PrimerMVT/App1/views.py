from django.shortcuts import render
from django.http import HttpResponse
from .models import Padre, Madre, Hermana
from django.template import Context, Template, loader



# Create your views here.

def padre(request):

    padre=Padre(nombre="Juan", apellido="Herrera" , edad=80)
    padre.save()
    plantilla=loader.get_template('template1.html')
    diccionario={'nombre': padre.nombre, 'apellido': padre.apellido, 'edad': padre.edad}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def madre(request):

    madre=Madre(nombre="Alicia", apellido="Terrero" , edad=78)
    madre.save()
    plantilla=loader.get_template('template2.html')
    diccionario={'nombre': madre.nombre, 'apellido': madre.apellido, 'edad': madre.edad}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def hermana(request):

    hermana=Hermana(nombre="Martha", apellido="Herrera" , edad=58)
    hermana.save()
    plantilla=loader.get_template('template3.html')
    diccionario={'nombre': hermana.nombre, 'apellido': hermana.apellido, 'edad': hermana.edad}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

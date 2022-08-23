from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Padre, Madre, Hermana


# Create your views here.

def padre(request):

    padre=Padre(nombre="Juan", apellido="Herrera" , edad=80)
    padre.save()
    texto=f"El padre fue creado: nombre: {padre.nombre} apellido: {padre.apellido}"
    return HttpResponse(texto)

def madre(request):

    madre=Madre(nombre="Alicia", apellido="Terrero" , edad=78)
    madre.save()
    texto=f"La madre fue creada: nombre: {madre.nombre} apellido: {madre.apellido}"
    return HttpResponse(texto)

def hermana(request):

    hermana=Hermana(nombre="Martha", apellido="Herrera" , hermana=58)
    hermana.save()
    texto=f"La hermana fue creada: nombre: {hermana.nombre} apellido: {hermana.apellido}"
    return HttpResponse(texto) 
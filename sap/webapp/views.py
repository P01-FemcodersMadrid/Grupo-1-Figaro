from django.shortcuts import render
from webapp.models import *
from django.http import HttpResponse


# Create your views here.

def login(request):
    # return HttpResponse('Holaaa')
    return render(request, 'index.html')


def inicio(request):
    # return HttpResponse('Holaaa')
    return render(request, 'home.html')


def perfil(request):
    nombre_profesor = Profesor.objects.all()
    return render(request, 'perfil.html', {'profesor': nombre_profesor})


def registro(request):
    return render(request, 'registro.html')


def contraseña(request):
    return render(request, 'contraseña.html')


def recuperada(request):
    return render(request, 'recuperada.html')

def alumnos(request):
    nombre_alumnos = Alumnos.objects.all()
    return render(request, 'alumnos.html', {'alumnos': nombre_alumnos})
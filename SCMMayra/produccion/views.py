from django.shortcuts import render
from .models import Disenio, Planeacion, Corte, Confeccion
from django.views.generic import ListView

# Creando las vistas que renderizarán los templates
class disenio(ListView):
    model=Disenio

class planeacion(ListView):
    model=Planeacion

class corte(ListView):
    model=Corte

class confeccion(ListView):
    model=Confeccion
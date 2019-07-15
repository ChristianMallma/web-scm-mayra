from django.shortcuts import render
from django.views.generic import ListView
from .models import Tienda,Carro,Transporte

# Creando vistas del módulo de distribución
class TiendaList(ListView):
    model=Tienda

class CarroList(ListView):
    model=Carro

class TransporteList(ListView):
    model=Transporte
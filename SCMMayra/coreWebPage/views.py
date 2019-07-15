from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Creando nuestras vistas
class Home(TemplateView):
    template_name="coreWebPage/home.html"

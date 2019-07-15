from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

#Aquí se colocará las vistas o clases del core
class Home(TemplateView):
        template_name="core/home.html"


   
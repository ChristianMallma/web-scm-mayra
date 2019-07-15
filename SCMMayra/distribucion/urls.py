from django.urls import path
from . import views
from .views import TiendaList,CarroList,TransporteList

urlpatterns = [
    path('tiendas/', TiendaList.as_view(), name="tiendas"),
    path('carros/', CarroList.as_view(), name="carros"),
    path('transportes/', TransporteList.as_view(), name="transportes"),
]
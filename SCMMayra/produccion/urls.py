from django.urls import path
from . import views
from .views import disenio,planeacion,corte,confeccion

urlpatterns = [
    path('registro/diseño/', disenio.as_view(), name="disenio"),
    path('registro/planeacion/', planeacion.as_view(), name="planeacion"),
    path('registro/corte/', corte.as_view(), name="corte"),
    path('registro/confeccion/', confeccion.as_view(), name="confeccion"),
]
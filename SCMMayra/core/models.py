from django.db import models

# Creando modelo que se repite
class ClaseModelo(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

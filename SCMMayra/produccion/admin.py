from django.contrib import admin
from .models import Disenio,Planeacion,Corte,Confeccion
from django.forms import Textarea
from django.db import models

# Registrando los modelos en el administrador
class DisenioAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class PlaneacionAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class CorteAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

    formfield_overrides={
        models.TextField:{'widget':Textarea(attrs={'rows':8,'cols':40})},
    }

class ConfeccionAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

    formfield_overrides={
        models.TextField:{'widget':Textarea(attrs={'rows':6,'cols':30})}
    }

admin.site.register(Disenio,DisenioAdmin)
admin.site.register(Planeacion,PlaneacionAdmin)
admin.site.register(Corte,CorteAdmin)
admin.site.register(Confeccion,ConfeccionAdmin)
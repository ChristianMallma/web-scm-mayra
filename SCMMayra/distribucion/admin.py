from django.contrib import admin
from .models import Tienda,Carro,Transporte

# Registrando modelo en el administrados
class TiendaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class CarroAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class TransporteAdmin(admin.ModelAdmin):
    readonly_fields=("fecha","modificacion")

admin.site.register(Transporte,TransporteAdmin)
admin.site.register(Tienda,TiendaAdmin)
admin.site.register(Carro,CarroAdmin)
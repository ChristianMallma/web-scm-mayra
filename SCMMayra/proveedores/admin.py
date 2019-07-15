from django.contrib import admin
from .models import Proveedor,InventarioInsumos, InventarioInsumosBasicos

# Registrando los modelos al administrador
class ProveedorAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class InventarioInsumosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class InventarioInsumosBasicosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(InventarioInsumos,InventarioInsumosAdmin)
admin.site.register(InventarioInsumosBasicos,InventarioInsumosBasicosAdmin)

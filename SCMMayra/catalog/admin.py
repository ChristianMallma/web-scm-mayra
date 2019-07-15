from django.contrib import admin
from .models import Producto,Comentario,ImagenesProducto,CarritoCompras

# Registrando los modelos
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Comentario)
admin.site.register(ImagenesProducto)
admin.site.register(CarritoCompras)

from django.db import models
from produccion.models import Disenio

# Creando modelo para registrar tiendas
class Tienda(models.Model):
    nombre_tienda=models.CharField(max_length=200,verbose_name="Nombre de tienda")
    direccion=models.CharField(max_length=400,verbose_name="Dirección")
    telefono=models.CharField(max_length=200,verbose_name="Teléfono")

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Tienda"
        verbose_name_plural="Tiendas"
        ordering=["-created"]

    def __str__(self):
        return self.nombre_tienda

class Carro(models.Model):
    placa=models.CharField(max_length=200,verbose_name="Placa")
    color=models.CharField(max_length=200,verbose_name="Color")
    capacidad=models.IntegerField(verbose_name="Capacidad")

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Carro"
        verbose_name_plural="Carros"
        ordering=['-created']
    
    def __str__(self):
        return self.placa

class Transporte(models.Model):
    tienda=models.ForeignKey(Tienda,verbose_name="Tienda",on_delete=models.PROTECT)
    carro=models.ForeignKey(Carro,verbose_name="Carro",on_delete=models.PROTECT)
    disenio=models.ForeignKey(Disenio,verbose_name="Producto",on_delete=models.PROTECT)
    cantidad=models.IntegerField(verbose_name="Cantidad")
    fecha=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de envío")
    modificacion=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Transporte"
        verbose_name_plural="Transportes"
        ordering=['-fecha']
    
    def __str__(self):
        return "{}: recibió {} del diseño {}".format(self.tienda,self.cantidad,self.disenio)
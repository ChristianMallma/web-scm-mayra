from django.db import models

# Creando modelo para registrar un proveedor
class Proveedor(models.Model):
    nombre_empresa=models.CharField(max_length=200,verbose_name="Empresa")
    ruc=models.CharField(max_length=200,verbose_name="RUC")
    direccion=models.CharField(max_length=400,verbose_name="Dirección")
    telefono=models.CharField(max_length=200,verbose_name="Teléfono")
    correo=models.CharField(max_length=200,verbose_name="Correo electrónico")

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores"
        ordering=["-created"]

    def __str__(self):
        return self.nombre_empresa

class InventarioInsumos(models.Model):
    nombre_insumo=models.CharField(max_length=200,verbose_name="Nombre del insumo")
    cantidad=models.IntegerField(blank=False, null=False,verbose_name="Cantidad")
    precio_compra=models.DecimalField(max_digits=8,decimal_places=2,verbose_name="Precio de compra")
    proveedor=models.ForeignKey(Proveedor,verbose_name="Proveedor",on_delete=models.PROTECT)
    observacion=models.CharField(max_length=400,verbose_name="Observaciones",blank=True,null=True)

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Inventario de Insumo"
        verbose_name_plural="Inventario de Insumos"
        ordering=["-created"]

    def __str__(self):
        return self.nombre_insumo

class InventarioInsumosBasicos(models.Model):
    nombre_insumo=models.CharField(max_length=200,verbose_name="Nombre del insumo")
    cantidad=models.IntegerField(blank=False, null=False,verbose_name="Cantidad")
    precio_compra=models.DecimalField(max_digits=8,decimal_places=2,verbose_name="Precio de compra")
    proveedor=models.ForeignKey(Proveedor,verbose_name="Proveedor",on_delete=models.PROTECT)
    observacion=models.CharField(max_length=400,verbose_name="Observaciones",blank=True,null=True)

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Inventario de Insumo Básico"
        verbose_name_plural="Inventario de Insumos Básicos"
        ordering=["-created"]

    def __str__(self):
        return self.nombre_insumo
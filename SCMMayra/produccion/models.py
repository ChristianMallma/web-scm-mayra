from django.db import models
from proveedores.models import InventarioInsumos

# Creando los modelos que formarán parte de Producción.
class Disenio(models.Model):
    activo=models.BooleanField(default=True)
    nombre=models.CharField(max_length=200,verbose_name="Nombre del diseño")
    imagen=models.ImageField(upload_to="producción",verbose_name="Imagen del diseño")
    tallas=models.IntegerField(verbose_name="Tallas del diseño",blank=False,null=False)
    codigo_disenio=models.CharField(max_length=200,verbose_name="Código de diseño")
    observacion=models.CharField(max_length=400,verbose_name="Observaciones",blank=True,null=True)

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Diseño"
        verbose_name_plural="Diseños"
        ordering=["-created"]

    def __str__(self):
        return self.nombre
    
class Planeacion(models.Model):
    codigo=models.ForeignKey(Disenio,verbose_name="Código de diseño",on_delete=models.PROTECT)
    talla=models.IntegerField(verbose_name="Talla")
    cantidad=models.IntegerField(verbose_name="Cantidad")
    observaciones=models.CharField(max_length=400,blank=True,null=True,verbose_name="Observaciones")

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Planeación"
        verbose_name_plural="Planeaciones"
        ordering=["created"]

    def __str__(self):
        return "{} -Talla {}".format(self.codigo,self.talla)

class Corte(models.Model):
    nombre_disenio=models.ForeignKey(Disenio,verbose_name="Nombre del diseño",on_delete=models.PROTECT)
    nombre_insumo=models.ForeignKey(InventarioInsumos,verbose_name="Nombre de insumo",on_delete=models.PROTECT)
    talla_mesa=models.TextField(verbose_name="Tallas en mesa")
    estampado=models.TextField(max_length=200,verbose_name="Estampados")
    bordado=models.TextField(max_length=200,verbose_name="Bordados")

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Corte"
        verbose_name_plural="Cortes"
        ordering=['-created']
    
    def __str__(self):
         return "{}".format(self.nombre_disenio)

class Confeccion(models.Model):
    nombre_disenio=models.ForeignKey(Disenio, verbose_name="Nombre del diseño", on_delete=models.PROTECT)
    remalle=models.TextField(verbose_name="Remalle",blank=True,null=True)
    recta=models.TextField(verbose_name="Recta",blank=True,null=True)
    recubridora=models.TextField(verbose_name="Recubridora",blank=True,null=True)
    collaretera=models.TextField(verbose_name="Collaretera",blank=True,null=True)
    elastiquera=models.TextField(verbose_name="Elastiquera",blank=True,null=True)
    boton_ojal=models.TextField(verbose_name="Botón y ojal",blank=True,null=True)
    otros=models.TextField(verbose_name="Otros",blank=True,null=True)

    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="Confección"
        verbose_name_plural="confecciones"
        ordering=["-created"]
    
    def __str__(self):
        return "{}".format(self.nombre_disenio)
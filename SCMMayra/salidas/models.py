from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from core.models import ClaseModelo
from produccion.models import Disenio

# Creando modelos para las salidas

#Modelo para el encabezado de la boleta
class ComprobanteEnc(ClaseModelo):
    fecha_factura=models.DateField()
    cliente=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name="Encabezado de comprobante"
        verbose_name_plural="Encabezado de comprobantes"
    
    def __str__(self):
        return "{}".format(self.fecha_factura)

#Modelo para el detalle de la boleta
class ComprobanteDet(ClaseModelo):
    comprobante=models.ForeignKey(ComprobanteEnc,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=0)
    producto=models.ForeignKey(Disenio,on_delete=models.CASCADE)
    precio=models.DecimalField(max_digits=5,decimal_places=2,default=0)
    total=models.DecimalField(max_digits=5,decimal_places=2,default=0)

    class Meta:
        verbose_name="Detalle de comprobante"
        verbose_name_plural="Detalle de comprobantes"

    def __str__(self):
        return "{} - {}".format(self.comprobante,self.producto)
    
    def save(self):
        self.total=Decimal(self.cantidad)*Decimal(self.precio)
        super(ComprobanteDet, self).save()

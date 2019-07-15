from django.shortcuts import render
from django.http import HttpResponse
from .models import Proveedor, InventarioInsumos, InventarioInsumosBasicos
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

# Creando vistas o clases para renderizar

class proveedor(ListView):
    model=Proveedor

#Recordar llamar en el template con el nombre todo en minúscula
class insumosE(ListView):
    model=InventarioInsumos

class insumosB(ListView):
    model=InventarioInsumosBasicos

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Impresión de insumos básicos, para reportes
def insumosBasicosPrint(self,pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate,Paragraph,TableStyle, Table
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter

    response=HttpResponse(content_type="application/pdf")
    buff=io.BytesIO()
    doc=SimpleDocTemplate(buff,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        botMargin=18,)
    
    insumos=[]
    styles=getSampleStyleSheet()
    header=Paragraph("Listado de Insumos Básicos",styles["Heading1"])
    insumos.append(header)
    headings=('Nombre de insumo','Cantidad','Precio de compra','Observacion','Proveedor')
    if not pk:
        registros=[(p.nombre_insumo,p.cantidad,p.precio_compra,p.observacion,p.proveedor)
                    for p in InventarioInsumosBasicos.objects.all().order_by('pk')]
    else:
        registros=[(p.nombre_insumo,p.cantidad,p.precio_compra,p.proveedor,p.observacion)
                    for p in InventarioInsumosBasicos.objects.filter(id=pk).order_by('pk')]
    
    t=Table([headings]+registros)
    t.setStyle(TableStyle(
        [
            ('GRID',(0,0),(4,-1),1,colors.dodgerblue),
            ('LINEBELOW',(0,0),(-1,0),2,colors.darkblue),
            ('BACKGROUND',(0,0),(-1,0),colors.dodgerblue)
        ]
    ))

    insumos.append(t)
    doc.build(insumos)
    response.write(buff.getvalue())
    buff.close()
    return response
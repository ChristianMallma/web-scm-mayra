from django.urls import path
from . import views
from .views import insumosE,insumosB,proveedor,insumosBasicosPrint

urlpatterns = [
    path('registro/proveedor/', proveedor.as_view(), name="proveedor"),
    path('registro/insumos/exactos/', insumosE.as_view(), name="invInsumosE"),
    path('registro/insumos/basicos/', insumosB.as_view(), name="invInsumosB"),
    path('registro/insumos/print/', insumosBasicosPrint, name="invInsumosBPrint"),
]
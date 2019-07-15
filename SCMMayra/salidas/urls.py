from django.urls import path

from .views import ComprobanteList,ComprobanteNew,ComprobanteEdit
from . import views

urlpatterns = [
    path("clientes/",views.cliente,name="cliente"),
    path("comprobantes/",ComprobanteList.as_view(),name="comprobantes_list"),
    path("comprobante/new/",ComprobanteNew.as_view(),name="comprobante_new"),
    path("comprobante/edit/<int:pk>",ComprobanteEdit.as_view(),name="comprobante_edit"),
]

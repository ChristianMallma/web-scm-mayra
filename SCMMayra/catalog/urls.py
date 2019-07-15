from django.urls import path
from .views import ListadoProducto,DetalleProducto,ComentarioProducto,Ingresar,Salir,AniadirCarrito,ListarCarrito,ListarCarritoPendientes,ListarCarritoFinalizadas,EliminarCarrito,DetallePago

urlpatterns = [
    path("listadoProductos/",ListadoProducto.as_view(),name="listadoProductos"),
    path("detalleProducto/<int:pk>/",DetalleProducto.as_view(),name="detalleProducto"),
    path("crearComentario/",ComentarioProducto.as_view(),name="crearComentario"),
    path("ingresar/",Ingresar.as_view(),name="ingresar"),
    path("salir/",Salir.as_view(),name="salir"),
    path("aniadirCarrito/",AniadirCarrito.as_view(),name="aniadirCarrito"),
    path('listarCarrito/',ListarCarrito.as_view(),name='listarCarrito'),
    path('listarPendientes/',ListarCarritoPendientes.as_view(),name='listarPendientes'),
    path('listarFinalizados/',ListarCarritoFinalizadas.as_view(),name='listarFinalizados'),
    path('eliminarCarrito/<int:pk>/',EliminarCarrito.as_view(),name='eliminarCarrito'),
    path('detallePago/',DetallePago.as_view(),name='detallePago'),
]
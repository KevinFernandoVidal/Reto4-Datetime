from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio_view, name="inicio"),
    path("add_vehiculo/", vehiculo_add_view, name="add_vehiculo"),
    path("mis_vehiculos/", mis_vehiculos_view, name="mis_vehiculos"),
    path("factura/crear", fatura_add_view, name="facturacrear"),
    path("factura/", fatura_view, name="factura"),
    path("factura/detalles/<int:id_factura>", fatura_destalles_view, name="facturadetalles"),
    path("factura/servicio/<int:id_factura>", factura_servicio_view, name="facturaservicio"),
]
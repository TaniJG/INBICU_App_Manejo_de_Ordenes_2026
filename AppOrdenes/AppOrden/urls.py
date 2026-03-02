from django.urls import path

from . import views

urlpatterns = [
    #path("", views.revisarOrden, name="revisarOrden"),
    path("",views.listaOrdenes.as_view(), name="listaDeOrdenes")
]
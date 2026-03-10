from django.urls import path

from . import views

app_name = "AppOrden"
urlpatterns = [
    #path("", views.revisarOrden, name="revisarOrden"),
    path("",views.ListaOrdenes.as_view(), name="listaOrdenes"),
    path("modificar/<int:pk>",views.ModificarOrden.as_view(),name="modificarOrden"),
    path("crear",views.CrearOrden.as_view(), name="crearOrden")
]
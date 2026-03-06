from .models import OrdenPaciente
from django.db.models import F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView

#Forma original de la view
"""def revisarOrden(request):
    lista_ordenes = OrdenPaciente.objects.order_by(id)
    context = {"lista_ordenes":lista_ordenes}
    return render(request, "AppOrden/revisarOrden.html",context)"""

"""class listaOrdenes(generic.ListView):
    template_name = "AppOrden/listaOrdenes.html"
    context_object_name = "lista_ordenes"
    def get_queryset(self):
        return OrdenPaciente.objects.order_by(OrdenPaciente.id)"""

class ListaOrdenes(generic.ListView):
    model = OrdenPaciente
    template_name = "AppOrden/listaOrdenes.html"
    def get_queryset(self):
        idIngresado = self.request.GET.get('q', '')
        object_list = self.model.objects.all()
        if idIngresado:
            object_list = object_list.filter(id=idIngresado)
        return object_list
    
class ModificarOrden(UpdateView):
    model = OrdenPaciente
    fields = ["nombrePaciente","apellidoPaciente","dniPaciente","numAfiliado","fechaOrden","nombreAnalisis"
            ,"nombreObraSocial","nombreMedico","firmaMedico","selloMedico"]
    template_name ="AppOrden\modificarOrden.html"

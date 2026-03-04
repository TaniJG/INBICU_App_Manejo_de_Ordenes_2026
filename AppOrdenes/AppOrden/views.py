from .models import OrdenPaciente
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

#Forma original de la view
"""def revisarOrden(request):
    lista_ordenes = OrdenPaciente.objects.order_by(id)
    context = {"lista_ordenes":lista_ordenes}
    return render(request, "AppOrden/revisarOrden.html",context)"""

class listaOrdenes(generic.ListView):
    template_name = "AppOrden/listaOrdenes.html"
    context_object_name = "lista_ordenes"
    def get_queryset(self):
        return OrdenPaciente.objects.order_by(OrdenPaciente.id)

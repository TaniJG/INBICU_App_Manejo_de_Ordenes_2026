from .models import OrdenPaciente
from .codificadores import codificar_analisis, codificar_OS
from django.db.models import F, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView
import AppOrden.verificaciones as verif
from django.contrib.auth.mixins import LoginRequiredMixin
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
#URL es localhost/AppOrden, por alguna razon
class ListaOrdenes(LoginRequiredMixin,generic.ListView):
    model = OrdenPaciente
    template_name = "AppOrden/listaOrdenes.html"
    #Buscador por ID y estado de la orden
    def get_queryset(self):
        idIngresado = self.request.GET.get('q', '')
        estadoFiltro = self.request.GET.get('estado', '') 
        
        object_list = list(self.model.objects.all())
        #Busca por ID
        if idIngresado:
            object_list = [orden for orden in object_list if str(orden.id) == idIngresado]
        
        # Filtrar por estado (completa/incompleta)
        if estadoFiltro == 'completa':
            object_list = [orden for orden in object_list if verif.verificacionTotal(orden)]
        elif estadoFiltro == 'incompleta':
            object_list = [orden for orden in object_list if not verif.verificacionTotal(orden)]
        
        return object_list
    #Solo tomar ordenes 
    #Revisa si la orden esta completa
    def verificarEstado(orden):        
        estadoOrden = verif.verificacionTotal(orden)
        return estadoOrden
    #Revisar todos los items para facilitar detección
    def verNomP(orden):
        return verif.verificacionNombrePac(orden)
    # Modifica lista generica para que el contexto incluya una verificacion
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega verificacion a los elementos como si fueran tuplas
        ordenes_estado = []
        ordenes_verificaciones = []
        for orden in context['object_list']:
            estado = verif.verificacionTotal(orden)
            ordenes_estado.append(estado)
            # Crear diccionario con verificación de cada campo
            verificaciones = {
                'nombrePaciente': verif.verificacionNombrePac(orden),
                'apellidoPaciente': verif.verificacionApellidoPac(orden),
                'dniPaciente': verif.verificacionDNIPac(orden),
                'numAfiliado': verif.verificacionNumAfiliado(orden),
                'fechaOrden': verif.verificacionFecha(orden),
                #'nombreAnalisis': verif.verificarAnalisisIndiv(orden.codigoAnalisis[0]) if orden.codigoAnalisis else False,
                'nombreAnalisis':True,
                'codigoAnalisis': verif.verificionAnalisisCompleto(orden),
                #'nombreObraSocial': verif.verificacionOS(orden),
                'nombreObraSocial': True,
                'codigoObraSocial': verif.verificacionOS(orden),
                'nombreMedico': verif.verificacionNombreMedico(orden),
                'firmaMedico': verif.verificacionFirmaMedico(orden),
                'selloMedico': verif.verificacionSelloMedico(orden),
            }
            ordenes_verificaciones.append(verificaciones)
        # Se crea una lista de tuplas (orden, estado, verificaciones) para iterar en el template html
        context['ordenes_con_estado'] = zip(context['object_list'], ordenes_estado, ordenes_verificaciones)
        return context

#Modificamos una orden existente
class ModificarOrden(LoginRequiredMixin,UpdateView):
    model = OrdenPaciente
    fields = ["nombrePaciente","apellidoPaciente","dniPaciente","numAfiliado","fechaOrden","nombreAnalisis"
            ,"nombreObraSocial","nombreMedico","firmaMedico","selloMedico"]
    template_name ="AppOrden/modificarOrden.html"
    success_url = "/AppOrden"
    
    def form_valid(self, form):
        # Guardar el formulario para obtener la instancia del objeto
        self.object = form.save()
        
        # Se codifica la Obra Social
        nombre_os = self.object.nombreObraSocial
        if nombre_os:
            codigo_os = codificar_OS(nombre_os)
            self.object.codigoObraSocial = codigo_os
        
        # Codificamos todos los Análisis
        nombre_analisis = self.object.nombreAnalisis
        if nombre_analisis and isinstance(nombre_analisis, list):
            codigos_analisis = []
            for nombre in nombre_analisis:
                codigo = codificar_analisis(nombre)
                codigos_analisis.append(codigo)
            self.object.codigoAnalisis = codigos_analisis
        
        # Guardar el objeto con los códigos actualizados
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

#Creamos una nueva orden
class CrearOrden(LoginRequiredMixin,CreateView):
    model = OrdenPaciente
    fields = ["nombrePaciente","apellidoPaciente","dniPaciente","numAfiliado","fechaOrden","nombreAnalisis"
            ,"nombreObraSocial","nombreMedico","firmaMedico","selloMedico"]
    template_name ="AppOrden/crearOrden.html"
    success_url = "/AppOrden"
    
    def form_valid(self, form):
        # Guardar el formulario para obtener la instancia del objeto
        self.object = form.save()
        
        # Se codifica la Obra Social
        nombre_os = self.object.nombreObraSocial
        if nombre_os:
            codigo_os = codificar_OS(nombre_os)
            self.object.codigoObraSocial = codigo_os
        
        # Codificamos todos los Análisis
        nombre_analisis = self.object.nombreAnalisis
        if nombre_analisis and isinstance(nombre_analisis, list):
            codigos_analisis = []
            for nombre in nombre_analisis:
                codigo = codificar_analisis(nombre)
                codigos_analisis.append(codigo)
            self.object.codigoAnalisis = codigos_analisis
        
        # Guardar el objeto con los códigos actualizados
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())
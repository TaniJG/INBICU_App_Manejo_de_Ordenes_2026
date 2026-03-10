from .models import OrdenPaciente
import datetime

def verificacionFecha(orden:OrdenPaciente):
    periodoVencim = 30
    periodo =  (datetime.date.today() - orden.fechaOrden)
    if periodo.days <= periodoVencim:
        return True
    else:
        return False
def verificacionNombrePac(orden: OrdenPaciente):
    if orden.nombrePaciente:
        return True
    else:
        return False
def verificacionApellidoPac(orden: OrdenPaciente):
    if orden.apellidoPaciente:
        return True
    else:
        return False
def verificacionDNIPac(orden: OrdenPaciente):
    if orden.dniPaciente:
        return True
    else:
        return False
def verificacionNumAfiliado(orden: OrdenPaciente):
    if orden.numAfiliado:
        return True
    else:
        return False
def verificacionNombreMedico(orden: OrdenPaciente):
    if orden.nombreMedico:
        return True
    else:
        return False
def verificacionFirmaMedico(orden: OrdenPaciente):
    if orden.firmaMedico:
        return True
    else:
        return False
def verificacionSelloMedico(orden: OrdenPaciente):
    if orden.selloMedico:
        return True
    else:
        return False
def verificacionOS(orden: OrdenPaciente):
    if orden.codigoObraSocial > 0:
        return True
    else:
        return False
    
def verificarAnalisisIndiv(codAnalisis): #Este es por variable ya que se repetira dentro de un for para determinar todas los analisis sin cubrir
    if codAnalisis > 1:
        return True
    else:
        return False

def verificionAnalisisCompleto(orden:OrdenPaciente):
    analisisCorrecto = 0
    for codAn in orden.codigoAnalisis:
            if verificarAnalisisIndiv(codAn):
                analisisCorrecto += 1
    if (analisisCorrecto == len(orden.codigoAnalisis)):
        return True
    else:
        return False

def verificacionCamposId(orden:OrdenPaciente):
    if verificacionNombrePac(orden) and verificacionApellidoPac(orden) and verificacionDNIPac(orden) and verificacionNumAfiliado(orden) and verificacionNombreMedico(orden) and verificacionFirmaMedico(orden) and verificacionSelloMedico(orden):
        return True
    else:
        return False
    
def verificacionTotal(orden:OrdenPaciente):
    if verificacionCamposId(orden) and verificacionFecha(orden) and verificacionOS(orden) and verificionAnalisisCompleto(orden):
        return True
    else:
        return False
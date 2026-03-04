from .models import OrdenPaciente
import codificadores

#Utiliza los datos recolctados para crear una orden en la base de datos
def crear_orden(nomPac,apellidoPac,dniPac,numAfil,fechaO,nomAn,nomOS,nomMed,firmaMed,selloMed):
    codAn =[]
    i = 0
    for nom in nomAn:
        codAn.append(codificadores.codificar_analisis(nom)) 
    codOS = codificadores.codificar_OS(nomOS)
    op = OrdenPaciente.objects.create(
        nombrePaciente = nomPac,
        apellidoPaciente = apellidoPac,
        dniPaciente = dniPac,
        numAfiliado = numAfil,
        fechaOrden = fechaO,
        nombreAnalisis = nomAn,
        codigoAnalisis = codAn,
        nombreObraSocial = nomOS,
        codigoObraSocial = codOS,
        nombreMedico = nomMed,
        firmaMedico = firmaMed,
        selloMedico = selloMed
    )
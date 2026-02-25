import orden as orden
import fecha_auditoria as fecha_aud
import analisis as analisis
import obra_social as OS


def cargar_paciente(nombre, apellido, dni):
    paciente = orden.Paciente(nombre, apellido, dni)
    return paciente

def cargar_fecha(fecha):
    fechaAud = fecha_aud.Fecha_auditoria(fecha)
    return fechaAud

def cargar_analisis(nombre):
    analisisO = analisis.Analisis(nombre)
    return analisisO

def cargar_obra_social(nombre):
    obra_social = OS.Obra_social(nombre)
    return obra_social

def cargar_orden(nombrePac:str,apellidoPac:str,dniPac:int,numAfiliado:int,fechaOrd:str,nombreAnalisis:str,nombreOS:str,nombreMed:str,firmaMed:bool,selloMed:bool):
    paciente = cargar_paciente(nombrePac,apellidoPac,dniPac)
    fecha = cargar_fecha(fechaOrd)
    analisisOr = cargar_analisis(nombreAnalisis)
    obraSocial =cargar_obra_social(nombreOS)
    instanciaOrden = orden.Orden(paciente,numAfiliado,fecha,analisisOr,obraSocial,nombreMed,firmaMed,selloMed)
    return instanciaOrden
import orden as orden
import carga_orden as cargarO
import almacenar_orden as almacenarO
import datetime as date

nombrePaciente = "Carlos"
apellidoPaciente = "Carlos"
dniP = 76666666
paciente = cargarO.cargar_paciente(nombrePaciente,apellidoPaciente,dniP)
n_afil = 343
fecha = date.datetime.today()
fechaO = cargarO.cargar_fecha(fecha)
nomAnalisis ="ANGIOTENSINA I"
analisisP = cargarO.cargar_analisis(nomAnalisis)
nomObraSocial ="OSPPYFER PANADEROS"
OSPaciente = cargarO.cargar_obra_social(nomObraSocial)
nombreMedico = "Juan Medicina"
firmaMed = True
selloMed = True
ordenPrueba = orden.Orden(paciente,n_afil,fechaO,analisisP,OSPaciente,nombreMedico,firmaMed,selloMed)
ordenPrueba.codificar()
if (ordenPrueba.verificacion_de_orden()) and (ordenPrueba.verificacion_Fecha()) and (ordenPrueba.verificacion_datos_presentes()):
    almacenarO.insertar_orden_BD(ordenPrueba)
else:
    ordenPrueba.elemento_fuera_de_convenio()
    ordenPrueba.aviso_error_orden()

import fecha_auditoria as FA
import datetime as datet

#Exito
fechaElem = FA.Fecha_auditoria(datet.datetime(2026,2,10))
if fechaElem.Vencimiento_Fecha():
    print(str(fechaElem.fecha) + "es una fecha valida")
else:
    print(str(fechaElem.fecha) + "es una fecha vencida")

#Fallo
fechaElem = FA.Fecha_auditoria(datet.datetime(2025,2,10))
if fechaElem.Vencimiento_Fecha():
    print(str(fechaElem.fecha) + "es una fecha valida")
else:
    print(str(fechaElem.fecha) + "es una fecha vencida")

from django.test import TestCase
from django.urls import reverse
import datetime
from AppOrden.creadorDeOrdenes import crear_orden
# Create your tests here.
#Esto esta probablemente mal
def test_crear_orden_entera(): #Ponemos a prueba la funcion que deberia crear ordenes a partir de parametros
    crear_orden(
        "Carlos",
        "Carlos",
        45777888,
        343,
        datetime.datetime.today(),
        ["ADRENALINA, plasmática","ALDOSTERONA.","BICARBONATO."],
        "OSPPYFER PANADEROS",
        "Juan Medicinal",
        True,
        True
    )

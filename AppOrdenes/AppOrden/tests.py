from django.test import TestCase
from django.urls import reverse
import datetime
import csv
import os
import sys
import django

# Add AppOrden path for imports
sys.path.insert(0, 'C:/Users/tanig/OneDrive/Documentos/INBICU-PS/App-Codif/AppOrdenes')

# Configure Django settings before importing models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppOrdenesINBICU.settings')
django.setup()

from AppOrden.creadorDeOrdenes import crear_orden
from AppOrden.codificadores import codificar_analisis, codificar_OS
from AppOrden.verificaciones import verificacionCamposId, verificacionOS, verificionAnalisisCompleto
from AppOrden.models import Analisis, ObrasSociales, OrdenPaciente

# Create your tests here.

class BaseTestCase(TestCase):
    """Base test class with shared setUp for loading CSV data"""
    def setUp(self):
        """Load data from CSV files before running tests"""
        # Load Analysis data
        with open('AppOrdenes\AppOrden\NBU_2012.csv', encoding='utf-8') as ADB:
            reader = csv.reader(ADB, delimiter=';')
            for row in reader:
                if row and row[0] != 'CODIGO' and len(row) >= 2: 
                    try:
                        codigo = int(row[0].strip())
                    except ValueError:
                        continue
                    Analisis.objects.get_or_create(
                        codigoAnalisis = codigo,
                        determinAnalisis = row[1].strip() if len(row) > 1 else '',
                    )
        
        # Cargamos datos de obras sociales
        with open('AppOrdenes\AppOrden\BD_Obras_Sociales.csv', encoding='utf-8') as OSDB:
            reader = csv.reader(OSDB, delimiter=';')
            for row in reader:
                if row and row[0] != 'OBRA SOCIAL' and len(row) >= 2: 
                    try:
                        codigo = int(row[1].strip()) if row[1].strip() else 0
                    except ValueError:
                        continue
                    ObrasSociales.objects.get_or_create(
                        obraSocial = row[0].strip() if row[0] else '',
                        codigoOS = codigo,
                    )

class TestsOrdenes(BaseTestCase):
    # setUp is now inherited from BaseTestCase
    def setUp(self):
        super().setUp()
        self.crear_orden_para_tests()
        self.crear_orden_erronea()
    #Creamos una orden de ejemplo
    def crear_orden_para_tests(self):
        crear_orden(
            "Carlos",
            "Carlos",
            45777888,
            343,
            datetime.datetime.today(),
            ["ACTO BIOQUÍMICO","ALDOSTERONA.","BICARBONATO."],
            "OSPPYFER PANADEROS",
            "Juan Medicinal",
            True,
            True)
    def crear_orden_erronea(self):
        crear_orden(
            "Carlos",
            "",
            999999999,
            344,
            datetime.datetime.today(),
            ["Homeopatia","ALDOSTERONA.","BICARVONATO."],
            "Social Obrerro",
            "Juan Medicinal",
            False,
            True)
    
    #TEST DE EXITO

    #La orden tiene los componentes necesarios, por lo cual deberia pasar
    def test_orden_con_campos_verificada(self): 
        ordenCreada = OrdenPaciente.objects.get(id = 1)
        self.assertIs(verificacionCamposId(ordenCreada), True)
    #La OS deberia tener su código
    def test_os_codificada_correctamente(self):
        ordenCreada = OrdenPaciente.objects.get(id = 1)
        self.assertIs(verificacionOS(ordenCreada),True)
    #Todos los analisis deberian estar codificados
    def test_analisis_codificados_correctamente(self):
        ordenCreada = OrdenPaciente.objects.get(id = 1)
        self.assertIs(verificionAnalisisCompleto(ordenCreada),True)
    
    #TEST DE FALLO

    #Faltan datos, deberia salir mal
    def test_fallo_campos_verificada(self): 
        ordenCreada = OrdenPaciente.objects.get(id = 2)
        self.assertIs(verificacionCamposId(ordenCreada), False)
    
    def test_os_incorrecta_sin_codigo(self):
        ordenCreada = OrdenPaciente.objects.get(id = 2)
        self.assertIs(verificacionOS(ordenCreada),False)
    def test_analisis_incorrectos_sin_codigo(self):
        ordenCreada = OrdenPaciente.objects.get(id = 2)
        self.assertIs(verificionAnalisisCompleto(ordenCreada),False)


class TesteoCodificacion(BaseTestCase):
    # setUp is now inherited from BaseTestCase
    def test_codificacion_analisis(self):
        #Al ingresar un nombre se deberia obtener el código correcto
        nombre = "ALDOSTERONA."
        codigo = codificar_analisis(nombre)
        self.assertEqual(codigo,660019)
    def test_codificacion_os(self):
        #Al ingresar un nombre se deberia obtener el código correcto
        nombre = "OSPE GUALEGUAYCHU"
        codigo = codificar_OS(nombre)
        self.assertEqual(codigo,1008)

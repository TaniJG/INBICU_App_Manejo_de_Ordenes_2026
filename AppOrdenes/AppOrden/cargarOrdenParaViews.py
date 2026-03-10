#Este codigo tiene como objetivo cargar una orden a la base de datos para realizar pruebas con las views, y asegurarse que funcionen correctamente
import datetime
import os
import sys
import django

# Agregamos la carptera AppOrdenes al Python path para importar AppOrdenesINBICU
sys.path.insert(0, 'C:/Users/tanig/OneDrive/Documentos/INBICU-PS/App-Codif/AppOrdenes')

# Se configura Django settings antes de  importar modelos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppOrdenesINBICU.settings')
django.setup()
from AppOrden.creadorDeOrdenes import crear_orden
from AppOrden.models import OrdenPaciente
crear_orden("Miguel",
            None,
            45454545,
            349,
            datetime.datetime.today(),
            ["ACTO BIOQUÍMICO"],
            "POLICIA FEDERAL ",
            "Victor Apellido",
            None,
            True)





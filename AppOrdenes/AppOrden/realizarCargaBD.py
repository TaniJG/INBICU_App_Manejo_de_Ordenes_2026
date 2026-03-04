import os
import sys
import django

# Agregamos la carptera AppOrdenes al Python path para importar AppOrdenesINBICU
sys.path.insert(0, 'C:/Users/tanig/OneDrive/Documentos/INBICU-PS/App-Codif/AppOrdenes')

# Se configura Django settings antes de  importar modelos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppOrdenesINBICU.settings')
django.setup()

from AppOrden.cargarBDDeCodif import importar_analisis, importar_OS

importar_analisis()
importar_OS()


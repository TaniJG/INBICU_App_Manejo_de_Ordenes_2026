import csv
from .models import Analisis, ObrasSociales

#Pasamos los datos de los .csv a las tablas de la Base de Datos
def importar_OS():
    with open('C:/Users/tanig/OneDrive/Documentos/INBICU-PS/App-Codif/BD_Obras_Sociales.csv', encoding='utf-8') as OSDB: #Este path solo aplica a este computador
        reader = csv.reader(OSDB, delimiter=';')
        for row in reader:
            if row and row[0] != 'OBRA SOCIAL' and len(row) >= 2: 
                try:
                    codigo = int(row[1].strip()) if row[1].strip() else 0
                except ValueError:
                    continue  # Skip invalid codes
                _, created = ObrasSociales.objects.get_or_create(
                    obraSocial = row[0].strip() if row[0] else '',
                    codigoOS = codigo,
                    )

def importar_analisis():
    with open('C:/Users/tanig/OneDrive/Documentos/INBICU-PS/App-Codif/NBU_2012.csv', encoding='utf-8') as ADB: #Este path solo aplica a este computador
        reader = csv.reader(ADB, delimiter=';')
        for row in reader:
            if row and row[0] != 'CODIGO' and len(row) >= 2: 
                try:
                    codigo = int(row[0].strip())
                except ValueError:
                    continue  # Skip invalid codes
                _, created = Analisis.objects.get_or_create(
                    codigoAnalisis = codigo,
                    determinAnalisis = row[1].strip() if len(row) > 1 else '',
                    )

import mysql.connector
import csv

# Nos conectamos a la Base de datos
mydb = mysql.connector.connect(
  host ='localhost',
  user ='root',
  password ='',
  database =  'nbu-2012_proyecto_inbicu'
)

myCursor = mydb.cursor()
#Creamos la tabla de OSs 
crear_tabla = """
CREATE TABLE IF NOT EXISTS BD_OS (
    `OBRA SOCIAL` TEXT,
    `COD.` VARCHAR(4)  PRIMARY KEY
)
"""
myCursor.execute(crear_tabla)
#Importamoes el archivo csv
csv_file = 'BD_Obras_Sociales.csv'

insertar_sql = "INSERT IGNORE INTO BD_OS (`OBRA SOCIAL`, `COD.`) VALUES (%s, %s)"


with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # Saltar cabecera
    
    for row in reader:
        if len(row) >= 2 and row[0].strip():  # Asegura que la fila no esta vacia
            obra_social = row[0].strip()
            cod= row[1].strip() if len(row) > 1 else ''
            try:
                myCursor.execute(insertar_sql, (obra_social,cod))
            except Exception as e:
                print(f"Error inserting row {obra_social}: {e}")

mydb.commit()

# Verify the import
myCursor.execute("SELECT COUNT(*) FROM BD_OS")
result = myCursor.fetchone()
print(f"Total rows in table: {result[0]}")

myCursor.close()
mydb.close()


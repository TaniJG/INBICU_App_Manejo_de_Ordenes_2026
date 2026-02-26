import mysql.connector

# Nos conectamos a la Base de datos
mydb = mysql.connector.connect(
  host ='localhost',
  user ='root',
  password ='',
  database =  'ordenes_almacenadas'
)

myCursor = mydb.cursor()
#Creamos la tabla de OSs 
crear_tabla = """
CREATE TABLE IF NOT EXISTS ORDENES (
    `ID ORDEN` INT AUTO_INCREMENT PRIMARY KEY,
    `NOMBRE PACIENTE` TEXT,
    `APELLIDO PACIENTE` TEXT,
    `DNI` VARCHAR(8),
    `N° AFILIADO` INT,
    `FECHA` VARCHAR(20),
    `NOMBRE ANALISIS` TEXT,
    `CODIGO ANALISIS` VARCHAR(20),
    `OBRA SOCIAL` TEXT,
    `CODIGO OBRA SOCIAL` VARCHAR(4),
    `NOMBRE MÉDICO` TEXT,
    `FIRMA MÉDICO` BOOL,
    `SELLO MÉDICO` BOOL
)
"""
myCursor.execute(crear_tabla)
myCursor.close()
mydb.close()


import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database= 'nbu-2012_proyecto_inbicu'
)
myCursor = mydb.cursor()

class Obra_social:
    def __init__(self,nombre):
        self.nombre = nombre
    def verificar_OS(self):
        pedido = "SELECT 'OBRA SOCIAL' FROM BD_OS WHERE `OBRA SOCIAL` = %s"
        myCursor.execute(pedido, (self.nombre,))
        nombreOSBD = myCursor.fetchone()
        if nombreOSBD:
            return True
        else:
            return False
    def agregar_id(self):
        pedido = "SELECT `COD.` FROM BD_OS WHERE `OBRA SOCIAL` = %s"
        myCursor.execute(pedido, (self.nombre,))
        idOS = myCursor.fetchone()
        if idOS:
            self.codigo = idOS[0]
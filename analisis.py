import mysql.connector


class Analisis:
    def __init__(self,nombre):
        self.nombre = nombre
    def codificacion(self):
        mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database= 'nbu-2012_proyecto_inbicu'
        )
        myCursor = mydb.cursor()
        pedido = "SELECT `CODIGO` FROM nbu_2012 WHERE `DETERMINACIONES` = %s"
        myCursor.execute(pedido, (self.nombre,))
        codigo = myCursor.fetchone()
        if codigo:
            self.codigo = codigo[0]
        else:
            print("Análisis fuera de convenio")
        myCursor.close()
        mydb.close()

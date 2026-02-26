import orden as ordenPac
import mysql.connector


def insertar_orden_BD(orden: ordenPac.Orden):
    mydb = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='',
    database =  'ordenes_almacenadas'
    )
    myCursor=mydb.cursor()
    insertar_sql ="""INSERT INTO ORDENES 
    (`NOMBRE PACIENTE`,
    `APELLIDO PACIENTE`,
    `DNI`,
    `N° AFILIADO`,
    `FECHA`,
    `NOMBRE ANALISIS` ,
    `CODIGO ANALISIS` ,
    `OBRA SOCIAL` ,
    `CODIGO OBRA SOCIAL` ,
    `NOMBRE MÉDICO` ,
    `FIRMA MÉDICO` ,
    `SELLO MÉDICO`)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    myCursor.execute(insertar_sql,(orden.paciente.nombre,orden.paciente.apellido,orden.paciente.dni,orden.n_afiliado,orden.fechaAud.fecha,orden.analisisPaciente.nombre,orden.analisisPaciente.codigo,orden.obraSocial.nombre,orden.obraSocial.codigo,orden.nombreMed,orden.firmaMed,orden.selloMed))
    mydb.commit()
    print("Almacenamiento realizado")
    myCursor.close()
    mydb.close()
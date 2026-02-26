import fecha_auditoria as fecha_aud
import analisis as analisis
import obra_social as OS

class Paciente:
    apellido: str
    nombre: str
    dni: int
    def __init__(self,apellido:str,nombre:str,dni:int):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
# Limitar el tipo de variable
class Orden:
    def __init__(self, paciente:Paciente,numAfiliado:int,fechaAud:fecha_aud.Fecha_auditoria,analisisPaciente:analisis.Analisis,obraSocial:OS.Obra_social,nombreMed:str,firmaMed:bool,selloMed:bool): 
        self.paciente = paciente
        self.n_afiliado = numAfiliado
        self.fechaAud = fechaAud
        self.analisisPaciente = analisisPaciente
        self.obraSocial = obraSocial
        self.nombreMed = nombreMed
        self.firmaMed = firmaMed
        self.selloMed = selloMed

    #def determinar_obra_social(): #Se elegira de una lista preexistente de Obras
        #pass
    def codificar(self): #Analisis se cargara el nombre, y código tendra carga inicial ""
        self.analisisPaciente.codificacion()
    def verificacion_OS(self):
        self.obraSocial.verificar_OS()
    def verificacion_Fecha(self):
        return self.fechaAud.Vencimiento_Fecha() 
    def verificacion_datos_presentes(self):
        if (self.paciente.apellido !="") and (self.paciente.nombre !="") and (self.nombreMed !="") and self.firmaMed and self.selloMed:
            return True
        else: 
            return False
    def verificacion_de_orden(self):
        if (self.obraSocial.verificar_OS()):
            self.obraSocial.agregar_id()
            return True
        else:
            return False
    def elemento_fuera_de_convenio(self):
        if not(self.analisisPaciente.codigo):
            print("Este análisis no se encuentra cubierto")
        if not(self.verificacion_de_orden()):
            print("Obra Social no esta cubierta") 
    def aviso_error_orden(self):
        if not(self.verificacion_Fecha()):
            print("Orden Vencida")
        if not(self.verificacion_datos_presentes()):
            print("Datos Insuficientes") #Expandir para que diga especificamente que falla
        #Estos prints no deben estar presentes en el producto final, representan el mensaje que debe enviarse al usuario


    

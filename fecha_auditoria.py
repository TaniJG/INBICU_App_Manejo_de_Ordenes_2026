import datetime as date

class Fecha_auditoria:
    def __init__(self,fecha):
        self.fecha = fecha

    #def dar_periodo_vencimiento():
        #return 30
    
    def Vencimiento_Fecha(self):
        periodo_vencimiento = 30
        periodo = (date.datetime.today() - self.fecha)
        if periodo.days <= periodo_vencimiento:
            return True
        else:
            return False 
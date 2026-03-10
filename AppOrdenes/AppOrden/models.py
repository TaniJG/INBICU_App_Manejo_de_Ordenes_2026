from django.db import models


# Create your models here.
class OrdenPaciente(models.Model):
    nombrePaciente = models.CharField("Nombre",max_length=100, null=True, blank=True)
    apellidoPaciente = models.CharField("Apellido",max_length=100,null=True, blank=True)
    dniPaciente = models.IntegerField("DNI", null=True, blank=True)
    numAfiliado = models.IntegerField("N° de Afiliado",null=True,default=0, blank=True)
    fechaOrden = models.DateField("Fecha de la Orden",null=True, blank=True)
    nombreAnalisis = models.JSONField(default=list,null=True, blank=True)
    codigoAnalisis = models.JSONField(default=list,null=True, blank=True)
    nombreObraSocial = models.CharField("Obra Social",max_length=200,null=True, blank=True)
    codigoObraSocial = models.IntegerField("Código de OS",null=True, blank=True)
    nombreMedico = models.CharField("Nombre del Médico",max_length=200,null=True, blank=True)
    firmaMedico = models.BooleanField("Firma del Médico",null=True, blank=True)
    selloMedico = models.BooleanField("Sello del Médico",null=True, blank=True)
    def __str__(self):
        return str(self.id)


class ObrasSociales(models.Model):
    obraSocial = models.CharField("Obra Social",max_length=400)
    codigoOS = models.IntegerField("Código de OS")
    def __str__(self):
        return self.obraSocial

class Analisis(models.Model):
    determinAnalisis = models.CharField("Análisis",max_length=200)
    codigoAnalisis = models.IntegerField("Código del Análisis")
    def __str__(self):
        return self.determinAnalisis

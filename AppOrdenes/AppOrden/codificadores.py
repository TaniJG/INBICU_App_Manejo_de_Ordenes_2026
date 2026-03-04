from .models import ObrasSociales, Analisis

#Obtenemos los codigos para los datos de la orden
def codificar_analisis(nombreAnalisis):
    try:
        analisis = Analisis.objects.get(determinAnalisis=nombreAnalisis)
        codigo = analisis.codigoAnalisis
    except Analisis.DoesNotExist:
        codigo = 0 #Si se implementean los sinonimos esto deberia modificarse
    except Analisis.MultipleObjectsReturned:
        codigo = 1 #Avisa que hay multiples analisis que responden al nombre, no deberia pasar
    return codigo

def codificar_OS(nombreOS):
    try:
        os = ObrasSociales.objects.get(ObrasSociaL=nombreOS)
        codigo = os.codigoOS
    except Analisis.DoesNotExist:
        codigo = 0 #Si se implementean los sinonimos esto deberia modificarse
    except Analisis.MultipleObjectsReturned:
        codigo = 1 #Avisa que hay multiples Obras Sociales que responden al nombre, no deberia pasar
    return codigo
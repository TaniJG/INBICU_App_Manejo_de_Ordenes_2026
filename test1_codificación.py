import analisis as analisis

trial1 = analisis.Analisis("HEMOGRAMA.")
trial1.codificacion()
print("El código de " + trial1.nombre  + " es " + str(trial1.codigo))
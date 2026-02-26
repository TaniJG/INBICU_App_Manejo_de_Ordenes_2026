import obra_social as OS

trial3 = OS.Obra_social("OSPE GUALEGUAYCHU")
trial3.agregar_id()
print("El código de " + trial3.nombre  + " es " + str(trial3.codigo))
if trial3.verificar_OS():
    print("Obra existe")
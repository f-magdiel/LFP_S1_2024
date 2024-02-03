

# ? Modo de apertura de archivos r: Solo lectura
# * Abrimos el archivo en modo lectura 
Archivo = open('ejemplo1.txt', 'r')
# ! Genera un error si el archivo no existe

# * Ahora leemos el archivo
var_1 = Archivo.read()
print(var_1)

# * Cerramos el archivo
Archivo.close()

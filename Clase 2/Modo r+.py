
# ? Modo r+: Lectura y escritura
Archivo = open('ejemplo1.txt', 'r+')

# ! Modo r+: Genera error si el archivo no existe
# * Leer el archivo
var_1 = Archivo.read()
print(1,var_1)

# * Escribir en el archivo
Archivo.write('Este es un ejemplo de escritura con R+\n')

# * Cerrar el archivo
Archivo.close()

# ? Abrir el archivo
Archivo = open('ejemplo1.txt', 'r+')

# * Leer el archivo
var_1 = Archivo.read()
print(2,var_1)

# * Cerrar el archivo
Archivo.close()
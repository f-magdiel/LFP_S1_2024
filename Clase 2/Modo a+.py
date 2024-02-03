
# ? Modo a: Agregar
# * Abrir el archivo en modo a+
Archivo = open('ejemplo1.txt', 'a+')
# ! Modo a: Agrega el contenido al final del archivo sin borrar el contenido anterior, crea el archivo si no existe

# * Volver al inicio del archivo para leer
Archivo.seek(0)

# * Leer el archivo
var_1 = Archivo.read()
print(var_1)

# * Escribir en el archivo
Archivo.write('Agregando texto con A+\n')

# * Cerrar el archivo
Archivo.close()
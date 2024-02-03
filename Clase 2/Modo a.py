
# ? Modo a: Agregar
# * Abrir el archivo
Archivo = open('ejemplo1.txt', 'a')
# ! Modo a: Agrega el contenido al final del archivo sin borrar el contenido anterior, crea el archivo si no existe

# * Escribir en el archivo
Archivo.write('\nAgregando texto con A\n')

# * Cerrar el archivo
Archivo.close()
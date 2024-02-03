
# ? Abre el archivo en modo escritura
Archivo = open('ejemplo1.txt', 'w')
# ! Modo w: Sobreescribe el archivo si existe, si no existe lo crea

# * Escribir en el archivo
Archivo.write('Lenguajes formales y de programacion\n')

# * Cerrar el archivo
Archivo.close()
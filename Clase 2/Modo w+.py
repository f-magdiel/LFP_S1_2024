
# ? Modo w+: Lectura y escritura
# * Abrir el archivo
Archivo = open('ejemplo1.txt', 'w+')
# ! Crea el archivo si no existe o sobrescribe su contenido.

# * Leer el archivo
Contenido = Archivo.read()
print(Contenido)
print('Contenido arriba')

# * Escribir en el archivo
Archivo.write('\nEscribiendo con W+\n')

# * Cerrar el archivo
Archivo.close()
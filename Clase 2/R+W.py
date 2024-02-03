
# ? Abrir el archivo en modo 'a+' (agregar y leer)
archivo = open('mi_archivo.mov', 'a+')

# * Agregar contenido al archivo
archivo.write("Este es un ejemplo de agregar contenido al final del archivo.\n")
archivo.write("Python es genial!\n")

# ! Volver al inicio del archivo para leer
archivo.seek(0)

# ? Leer y mostrar el contenido del archivo línea por línea usando readline()
print("Contenido del archivo (readline):")
linea = archivo.readline()
while linea:
    print(linea, end='') # * El bucle se ejecutará hasta que se devuelva una cadena vacía
    linea = archivo.readline()

# ?  Volver al inicio del archivo para leer usando readlines()
archivo.seek(0)
lineas = archivo.readlines()

# ! Cerrar el archivo
archivo.close()

print("\nContenido del archivo (readlines()):")
print(lineas)
for linea in lineas:
    print(linea, end='') # * El bucle se ejecutará hasta que se devuelva una cadena vacía


import os
import time
from Archivo import escribir_dot, convertir_svg, convertir_pdf
def menu():
    print("|--------------------------|")
    print("| Menu                     |")
    print("| 1) Generar el .dot       |")
    print("| 2) Convertir en svg      |")
    print("| 3) Converit en png       |")
    print("| 4) Salir                 |")
    print("|--------------------------|")
    print("Selecciona una opcion: ")
    return input()

def main():
    while True:
        opcion = menu()
        if opcion == "1":
            print("Escribiendo el archivo .dot")
            escribir_dot()
            time.sleep(2)
        elif opcion == "2":
            print("Convirtiendo el archivo .dot en .svg")
            convertir_svg()
            time.sleep(2)
        elif opcion == "3":
            print("Convirtiendo el archivo .dot en .pdf")
            convertir_pdf()
            time.sleep(2)
        elif opcion == "4":
            print("Adios")
            time.sleep(2)
            break
        else:
            print("Opcion invalida")
            time.sleep(2)

if __name__ == "__main__":
    main()

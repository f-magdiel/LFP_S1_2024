def desplegarNombre():
    print("Mi nombre es magdiel")
    input("Presione una tecla para continuar...")


def desplegarCarnet():
    print("Mi carnet es 201602919")
    input("Presione una tecla para continuar...")

def desplegarNombreCarnet():
    print("Mi nombre es magdiel y mi carnet es 201602919")
    input("Presione una tecla para continuar...")

def salir():
    print("Gracias por usar el programa")
    input("Presione una tecla para continuar...") 


def menu():
    print("=======================================")
    print("| LENGUAJES FORMALES Y DE PROGRAMACION |")
    print("| SECCION: B+                          |")
    print("=======================================")
    print("| 1. Desplegar nombre                  |")
    print("| 2. Desplegar carnet                  |")
    print("| 3. Desplegar nombre y carnet         |")
    print("| 4. Salir                             |")
    print("=======================================")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        desplegarNombre()
        menu()

    elif opcion == 2:
        desplegarCarnet()
        menu()

    elif opcion == 3:
        desplegarNombreCarnet()
        menu()

    elif opcion == 4:
        salir()

    else:
        print("Opcion incorrecta")
        menu()

    
menu()
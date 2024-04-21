from Instrucciones.Funcion import *
from Error.Errores import *
from Abstract.Lexema import *

global n_linea
global n_columna
global instrucciones
global lista_lexemas
global lista_errores

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []


def intruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0


    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char.isupper() or char.islower():       #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                n_columna += len(lexema) + 1
                puntero = 0

        elif char == '=':
            #! Armamos lexema como clase
            c = Lexema(char, n_linea, n_columna)

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char =="\t":
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        elif char == ' ' or char == '\r':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
        else:
            lista_errores.append(Errores(char,"Lexico", n_linea, n_columna))
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1


    return lista_lexemas

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == ' ' or char == ';':
            return lexema, cadena[len(puntero):]    #! si encuentra una  " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None



def operar():
    global lista_lexemas
    global instrucciones

    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'CrearDB':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            creardb2 = lista_lexemas.pop(0)
            func =  Funcion(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, creardb2.lexema, lexema.getFila(), lexema.getColumna())
            return func
    return None

def operar_():
    global instrucciones
    temp_instrucciones = []
    while True:
        operacion = operar()

        if operacion:
            temp_instrucciones.append(operacion)

        else:
            break
    instrucciones = temp_instrucciones

    return instrucciones

def getErrores():
    global lista_errores
    return lista_errores


instrucciones = intruccion("CrearDB ejemplo =  nueva CrearDB();   ")

resultado_instrucciones = operar_()


for respuesta in resultado_instrucciones:
    print(respuesta.ejecutarT())


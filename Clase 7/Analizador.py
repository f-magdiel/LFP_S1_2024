from Abstract.Lexema import *

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_errores = []


def instruccion_inicio(cadena):
    global n_linea
    global n_columna
    global lista_lexemas

    lexema = ''
    puntero = 0

    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char == '\"':       #! leemos nuestra cadena y al encontrar un "" que habre empieza a crear el token
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema(lexema, n_linea, n_columna)
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                n_columna += len(lexema) + 1
                puntero = 0





def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == ':' or char == '\"' or char == ' ':
            return lexema, cadena[len(puntero):]    #! si encuentra una  : o " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None
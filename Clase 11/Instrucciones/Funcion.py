from Error.Errores import *
from Abstract.Abstract  import Expression


class Funcion(Expression):

    def __init__(self, crear, nombre, igual, nueva, crear2, fila, columna):
        self.crear = crear
        self.nombre = nombre
        self.igual = igual
        self.nueva = nueva
        self.crear2 = crear2
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        if self.crear == 'CrearDB':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.crear2 == 'CrearDB()':
                            return 'use(' + self.nombre + ');'
                        else:
                            return 'Error: falta la palabra reservada CrearDB()'
                    else:
                        return 'Error: Falta la palabra reservada nueva'
                else:
                    return 'Error: Falta el simbolo ='
            else:
                return 'Error: Falta el nombre de la base de datos'
        else:
            return Errores(self.crear,"Sintactico", self.getFila(), self.getColumna())

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

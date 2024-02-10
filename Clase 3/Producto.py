# Definición de la clase Producto
class Producto:
    def __init__(self, producto, precio, cantidad):
        self.nombre = producto
        self.precio = precio
        self.cantidad = cantidad
        self.total = 0

# Creación de objetos
manzana = Producto("Manzana", 1000, 10)
# Acceso a los atributos
manzana.total = 100
print(manzana.nombre)
print(manzana.precio)
print(manzana.cantidad)
print(manzana.total)
# Creación de objetos
pera = Producto("Pera", 2000, 20)
# Acceso a los atributos
pera.total = 200
print(pera.nombre)
print(pera.precio)
print(pera.cantidad)

# Creación de una lista de objetos
lista_productos = [manzana, pera]
# Recorrido de la lista de objetos
for producto in lista_productos:
    print(producto.nombre)
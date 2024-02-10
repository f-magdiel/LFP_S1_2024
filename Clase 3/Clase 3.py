# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre):
        self._nombre = nombre

    def hacer_sonido(self):
        pass  # Aquí no se hace nada, es solo un marcador de posición

# Definición de las clases Perro y Gato que heredan de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    def obtener_info(self):
        return f"Vehículo: {self._marca} {self._modelo}"

# Definición de las clases Coche y Moto que heredan de Vehiculo
class Coche(Vehiculo):
    def obtener_info(self):
        return f"Coche: {self._marca} {self._modelo}"

class Moto(Vehiculo):
    def obtener_info(self):
        return f"Moto: {self._marca} {self._modelo}"

# Definición de la clase Persona con encapsulación
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def _obtener_informacion(self):
        return f"Persona: {self._nombre}, {self._edad} años"

# Función que demuestra el polimorfismo
def hacer_sonar(animal):
    return animal.hacer_sonido()

# Crear objetos y demostrar los conceptos de POO

# Creación de objetos Perro y Gato
perro = Perro("Firulais")
gato = Gato("Garfield")

# Uso del polimorfismo para hacer sonar a los animales
print(perro._nombre)
print(perro.hacer_sonido())
print(gato._nombre)
print(gato.hacer_sonido())

# Creación de objetos Coche y Moto
coche = Coche("Toyota", "Corolla")
moto = Moto("Honda", "CBR500R")

# Uso del polimorfismo para obtener información de los vehículos
vehiculos = [coche, moto]

for vehiculo in vehiculos:
    print(vehiculo.obtener_info())

# Creación de objeto Persona y uso de encapsulación para obtener información
persona = Persona("Juan", 30)
print(persona._obtener_informacion())

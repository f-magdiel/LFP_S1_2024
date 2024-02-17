import re

def validar_numero_telefono(numero):
    patron_numero = r'^\d{3}-\d{3}-\d{4}$'
    if re.match(patron_numero, numero):
        return True
    else:
        return False

# Ejemplos de números de teléfono para validar
numeros = ["123-456-7890", "555-123-4567", "9876-543-210", "123-45-6789"]

for numero in numeros:
    if validar_numero_telefono(numero):
        print(f"{numero} es un número de teléfono válido.")
    else:
        print(f"{numero} NO es un número de teléfono válido.")

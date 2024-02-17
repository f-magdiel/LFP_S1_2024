import re

# Texto que contiene direcciones de correo electrónico
texto = "Hola, mi correo es ejemplo1@example.com y puedes contactarme en ejemplo2@gmail.com."

# Expresión regular para encontrar direcciones de correo electrónico
patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Buscar todas las coincidencias de direcciones de correo electrónico en el texto
direcciones_email = re.findall(patron_email, texto)

# Imprimir las direcciones de correo electrónico encontradas
print(direcciones_email)
for direccion in direcciones_email:
    print(direccion)

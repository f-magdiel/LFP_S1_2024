import re

def extraer_etiquetas_html(codigo_html):
    patron_etiqueta = r'<[^>]+>'
    etiquetas = re.findall(patron_etiqueta, codigo_html)
    return etiquetas

# Fragmento de código HTML de ejemplo
codigo_html = """
<div class="contenedor">
    <h1>Título</h1>
    <p>Este es un párrafo <a href="https://www.ejemplo.com">con un enlace</a>.</p>
</div>
"""

etiquetas_encontradas = extraer_etiquetas_html(codigo_html)

print("Etiquetas encontradas:", etiquetas_encontradas)
for etiqueta in etiquetas_encontradas:
    print(etiqueta)

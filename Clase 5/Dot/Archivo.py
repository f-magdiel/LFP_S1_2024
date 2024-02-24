import os

def escribir_dot():
    contenido_dot = """
    digraph G {
    fontname="Helvetica,Arial,sans-serif"
    graph [
        rankdir = "LR"
    ];
    // Nodo de la tabla 1
    node [shape=plaintext];
    tabla1 [label=<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR>
                <TD COLSPAN="2" BGCOLOR="darkgreen"><FONT COLOR="white">The amazing spiderman</FONT></TD>
            </TR>
            <TR>
                <TD>2014</TD>
                <TD>Accion</TD>
            </TR>
        </TABLE>
    >];

    // Nodos para los nombres de los actores
    node [shape=box, style=filled, fillcolor=darkmagenta, fontcolor=white];
    andrew [label="Andrew"];
    emma_stone [label="Emma Stone"];

    // Aristas de la tabla de la película a los nombres de los actores
    tabla1 -> andrew;
    tabla1 -> emma_stone;
}
    """
    nombre_dot = "pelicula.dot"

    with open("Clase 5/"+nombre_dot,"w") as archivo_dot:
        archivo_dot.write(contenido_dot)

    print(f"Archivo DOT '{nombre_dot}' creado satisfactoriamente.")

def convertir_svg():
    # Obtener el directorio actual
    dir_actual = os.getcwd()
    # Cambiar al directorio que contiene los archivos
    os.chdir("Clase 5")
    # Definir los nombres de los archivos
    nombre_dot = "pelicula.dot"
    nombre_svg = "pelicula.svg"
    # Ejecutar el comando dot
    os.system(f"dot -Tsvg \"{nombre_dot}\" -o \"{nombre_svg}\"")
    # Regresar al directorio original
    os.chdir(dir_actual)
    print(f"Archivo SVG '{nombre_svg}' creado satisfactoriamente.")


def convertir_pdf():
    # Obtener el directorio actual
    dir_actual = os.getcwd()
    # Cambiar al directorio que contiene los archivos
    os.chdir("Clase 5")
    # Definir los nombres de los archivos
    nombre_dot = "pelicula.dot"
    nombre_pdf = "pelicula.pdf"
    # Ejecutar el comando dot
    os.system(f"dot -Tpdf \"{nombre_dot}\" -o \"{nombre_pdf}\"")
    # Regresar al directorio original
    os.chdir(dir_actual)
    print(f"Archivo PDF '{nombre_pdf}' creado satisfactoriamente.")



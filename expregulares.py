import re

carpeta_nombre = "Documentos\\"
archivo_nombre = "Peli.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()

# Expresión regular para buscar la palabra "obligada" o palabras que sigan el patrón M[eéa][xr]ic?[ao](nos)?
expresion_regular = re.compile(r"o[bv][lí]igad[ao]")
resultados_busqueda = expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))


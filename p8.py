import re

carpeta_nombre = "Documentos\\"
archivo_nombre = "Peli.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()


expresion_regular=re.compile(r"(el)?(los)? mundo?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))


expresion_regular=re.compile(r"\d+(,\d+)*(\.\d+)?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))


#hola profesor este es el ejemplo
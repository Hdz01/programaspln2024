archivo_nombre = "peli.txt"
with open(archivo_nombre, "r") as archivo:
    lineas_lista=archivo.readlines()
print(lineas_lista)

num_linea = 1
lineas_vacias = 0
lineas_texto = 0


lineas_totales = len(lineas_lista)
for linea in lineas_lista:
    if linea.strip() == "":
        print("Linea vacia")
        continue
    print("Linea", num_linea, ":", linea)
    num_linea = num_linea + 1

print("Lineas totales: ", lineas_totales)
print("Lineas vacias ", lineas_vacias)
print("Lineas con texto ", lineas_texto )
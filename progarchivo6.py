import os 
carpeta_nombre = "documentos\\"
archivos_lista = os.listdir(carpeta_nombre)
for archivo_nombre in archivos_lista:
    print(archivo_nombre)
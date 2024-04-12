import nltk
import matplotlib.pyplot as plt

carpeta_nombre = "Documentos\\"
archivo_nombre = "Peli.txt"

# Abrir el archivo y leer el texto
with open(carpeta_nombre + archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Tokenizar el texto usando un tokenizador genérico
tokens = nltk.word_tokenize(texto)
texto_nltk = nltk.Text(tokens)

# Calcular la distribución de frecuencia
distribucion = nltk.FreqDist(texto_nltk)

# Graficar la distribución de frecuencia
distribucion.plot(30, cumulative=False)
plt.show()

# Imprimir la frecuencia de la palabra "Instituto" (sensible a mayúsculas y minúsculas)
print(distribucion["Instituto"])

import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Pedir al usuario que introduzca la URL de la página web
url_pagina = input("Introduce la URL de la página web que deseas analizar: ")

# Obtener el contenido de la página web
respuesta = requests.get(url_pagina)
contenido_pagina = respuesta.text

# Extraer el texto de la página utilizando BeautifulSoup
soup = BeautifulSoup(contenido_pagina, "html.parser")
texto_pagina = soup.get_text()

# Guardar el texto extraído en un archivo de texto
with open("texto_pagina.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto_pagina)

# Cargar el texto del archivo
with open("texto_pagina.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Contar el número de palabras
num_palabras = len(word_tokenize(texto))

# Contar el número de líneas
num_lineas = texto.count('\n') + 1

print("Número de palabras en la página:", num_palabras)
print("Número de líneas de texto en la página:", num_lineas)

# Mostrar palabras de 3 o 4 caracteres
tokens = word_tokenize(texto)
palabras_3_4_caracteres = [token for token in tokens if len(token) in (3, 4)]
print("Palabras de 3 o 4 caracteres:", palabras_3_4_caracteres)

# Contar el número de veces que aparece una palabra específica
palabra_especifica = input("Introduce la palabra que deseas buscar en el texto: ").lower()
num_ocurrencias = texto.lower().count(palabra_especifica)
print("Número de veces que aparece la palabra '{}' en el texto:".format(palabra_especifica), num_ocurrencias)

print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
nltk.download("stopwords")
palabras_funcionales = set(stopwords.words("spanish"))
for palabra_funcional in palabras_funcionales:
    print(palabra_funcional)

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = word_tokenize(texto, language="spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print(tokens_limpios)
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(40)

import nltk 

import nltk
nltk.download('punkt')

carpeta_nombre = "Documentos\\"
archivo_nombre = "Peli.txt"


with open (carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()


tokens = nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)


palabras_total = len (tokens)
print("Total de palabras",palabras_total)
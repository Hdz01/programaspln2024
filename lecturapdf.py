import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import os

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')

# Función para extraer texto de un archivo PDF
def extraer_texto(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Función para realizar análisis de texto
def analizar_texto(texto):
    # Tokenización de palabras
    palabras = word_tokenize(texto)

    # Contar palabras totales
    total_palabras = len(palabras)

    # Obtener palabras únicas y contar su frecuencia
    fdist = FreqDist(palabras)
    palabras_unicas = fdist.hapaxes()

    # Distribución de frecuencia
    distribucion_frecuencia = fdist.most_common(20)

    # Graficar las 20 palabras más comunes
    palabras_comunes, frecuencias = zip(*distribucion_frecuencia)
    plt.figure(figsize=(10, 6))
    plt.bar(palabras_comunes, frecuencias)
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.title('20 Palabras Más Comunes')
    plt.xticks(rotation=45)
    plt.show()

    return total_palabras, palabras_unicas, distribucion_frecuencia

# Función principal
def main():
    # Solicitar al usuario que ingrese la ruta del archivo PDF
    pdf_path = input("Por favor, ingresa la ruta del archivo PDF: ").strip()

    # Verificar si la ruta ingresada es válida
    if not os.path.isfile(pdf_path):
        print("La ruta del archivo PDF no es válida.")
        return

    # Extraer texto del PDF
    try:
        texto_extraido = extraer_texto(pdf_path)
    except Exception as e:
        print("Error al extraer texto del PDF:", e)
        return

    # Realizar análisis de texto
    try:
        total_palabras, palabras_unicas, distribucion_frecuencia = analizar_texto(texto_extraido)
    except Exception as e:
        print("Error al analizar el texto:", e)
        return

    # Resultados
    print("Total de palabras:", total_palabras)
    print("Palabras que aparecen una sola vez:", palabras_unicas)
    print("Distribución de frecuencia de las 20 palabras más comunes:", distribucion_frecuencia)

if __name__ == "__main__":
    main()

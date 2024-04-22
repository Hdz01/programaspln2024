import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Descargar recursos de nltk
nltk.download('punkt')

# Función para extraer texto de un archivo PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

# Función para realizar análisis de texto
def analyze_text(text):
    # Tokenizar el texto en palabras
    words = word_tokenize(text)
    
    # Contar las palabras totales
    total_words = len(words)
    
    # Calcular la distribución de frecuencia de las palabras
    fdist = FreqDist(words)
    
    # Obtener palabras únicas
    unique_words = fdist.hapaxes()
    
    # Graficar las 20 palabras más comunes
    fdist.plot(20, cumulative=False)
    plt.show()
    
    return total_words, unique_words, fdist

# Ruta del archivo PDF
pdf_path = '2.pdf'

# Extraer texto del PDF
text = extract_text_from_pdf(pdf_path)

# Realizar análisis de texto
total_words, unique_words, fdist = analyze_text(text)

# Imprimir resultados
print("Número total de palabras:", total_words)
print("Palabras únicas:", len(unique_words))
print("Distribución de frecuencia:", fdist.most_common(20))

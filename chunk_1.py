import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import ne_chunk, pos_tag

# Descargar los recursos necesarios
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')

# Función para procesar el texto ingresado por el usuario
def process_text(text):
    # Tokenización y etiquetado POS (Part-Of-Speech)
    words = word_tokenize(text)
    tagged = pos_tag(words)

    # Definición de la gramática para frases sustantivas y verbales
    grammar = r"""
      NP: {<DT>?<JJ>*<NN>}
      VP: {<VB.*><NP|PP|CLAUSE>+$}
    """

    # Creación del analizador de chunking con múltiples patrones
    parser = RegexpParser(grammar)

    # Realizar el chunking
    chunked_result = parser.parse(tagged)

    # Realizar el chunking de entidades nombradas
    ner_chunks = ne_chunk(tagged)

    # Imprimir los resultados
    print("Chunking result:")
    print(chunked_result)
    print("\nNamed Entities result:")
    print(ner_chunks)

# Solicitar al usuario que ingrese el texto
user_input = input("Ingrese el texto que desea analizar: ")

# Procesar el texto ingresado por el usuario
process_text(user_input)

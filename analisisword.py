import nltk
from nltk import ne_chunk, pos_tag, word_tokenize

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encuentra.")
        return None

def extract_named_entities(text):
    # Tokenizar el texto en palabras
    tokens = word_tokenize(text)
    
    # Etiquetar las palabras con su parte del discurso (POS)
    pos_tags = pos_tag(tokens)
    
    # Identificar las entidades nombradas usando ne_chunk
    ner_chunks = ne_chunk(pos_tags)
    
    return ner_chunks

# Solicitar la ruta del archivo de texto al usuario
file_path = input("Introduce la ruta del archivo de texto (.txt): ")

# Leer el archivo de texto
text = read_file(file_path)

# Asegurarse de que el texto se haya leído correctamente
if text:
    # Extraer entidades nombradas
    named_entities = extract_named_entities(text)

    # Imprimir las entidades nombradas
    print(named_entities)

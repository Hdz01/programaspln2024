import docx 
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Function to count words and lines
def count_words_lines(text):
    num_words = len(text.split())
    num_lines = text.count('\n') + 1
    return num_words, num_lines


def count_word_frequency(text, word):
    return text.lower().count(word.lower())


document_path = input("Ingrese el nombre del documento word: ")


document = docx.Document(document_path)


text_document = ""
for paragraph in document.paragraphs:
    text_document += paragraph.text + "\n"

with open("text_document.txt", "w", encoding="utf-8") as file:
    file.write(text_document)


num_words, num_lines = count_words_lines(text_document)
print("Numero de palabras en el texto:", num_words)
print("Numero de lineas de texto en el texto:", num_lines)


searched_word = input("Ingres la palabra que quieres encontrar en el texto: ")
word_frequency = count_word_frequency(text_document, searched_word)
print("La palabra '{}' aparece {} veces en el documento.".format(searched_word, word_frequency))


nltk.download('stopwords')
nltk.download('punkt')
functional_words = set(stopwords.words("spanish"))


tokens = word_tokenize(text_document, language="spanish")
clean_tokens = [token for token in tokens if token.lower() not in functional_words]


print(clean_tokens)
print("Total number of tokens:", len(tokens))
print("Number of clean tokens:", len(clean_tokens))


clean_text_nltk = nltk.Text(clean_tokens)
clean_distribution = nltk.FreqDist(clean_text_nltk)


plt.figure(figsize=(10, 5))
clean_distribution.plot(20)
plt.show()

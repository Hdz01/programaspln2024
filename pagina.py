import requests
from bs4 import BeautifulSoup
import re

def contar_palabras(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        texto = soup.get_text()
        texto_limpio = re.sub(r'[^\w\s]', '', texto)
        palabras = texto_limpio.split()
        cantidad_palabras = len(palabras)
        return cantidad_palabras
    else:
        print("No se pudo obtener el contenido de la página.")
        return None

url = 'https://www.iic.uam.es/inteligencia/que-es-procesamiento-del-lenguaje-natural/'
cantidad_palabras = contar_palabras(url)
if cantidad_palabras is not None:
    print("La cantidad de palabras en la página web es:", cantidad_palabras)


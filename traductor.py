from googletrans import Translator

def traducir_texto(texto, idioma_destino):
    traductor = Translator()
    traduccion = traductor.translate(texto, dest=idioma_destino)
    return traduccion.text

if __name__ == "__main__":
    texto_a_traducir = input("Ingrese el texto que desea traducir: ")
    idioma_destino = input("Ingrese el código del idioma de destino (por ejemplo, 'es' para español, 'en' para inglés, 'fr' para frances, 'de' para aleman, 'it' para italiano, 'pt' para portugues): ")

    try:
        texto_traducido = traducir_texto(texto_a_traducir, idioma_destino)
        print(f"Texto traducido: {texto_traducido}")
    except Exception as e:
        print(f"Error al traducir el texto: {e}")

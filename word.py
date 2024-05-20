from gtts import gTTS
import os
import docx

def texto_a_audio(texto):
    # Inicializar el objeto gTTS
    tts = gTTS(text=texto, lang='es')
    
    # Guardar el archivo de audio
    tts.save("audio_generado.mp3")
    
    # Reproducir el archivo de audio
    os.system("start audio_generado.mp3")

def leer_archivo_txt(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    return texto

def leer_archivo_word(ruta):
    doc = docx.Document(ruta)
    texto = ""
    for paragraph in doc.paragraphs:
        texto += paragraph.text + "\n"
    return texto

def seleccionar_archivo():
    while True:
        opcion = input("Seleccione el tipo de archivo (1 para .txt, 2 para .docx): ")
        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo .txt: ")
            if os.path.exists(ruta):
                texto = leer_archivo_txt(ruta)
                texto_a_audio(texto)
                break
            else:
                print("El archivo no existe. Inténtelo de nuevo.")
        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo .docx: ")
            if os.path.exists(ruta):
                texto = leer_archivo_word(ruta)
                texto_a_audio(texto)
                break
            else:
                print("El archivo no existe. Inténtelo de nuevo.")
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")

# Seleccionar y convertir archivo a audio
seleccionar_archivo()

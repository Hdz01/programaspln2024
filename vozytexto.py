import speech_recognition as sr
from gtts import gTTS
import os

def audio_a_texto():
    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()
    
    # Abrir el archivo de audio
    with sr.AudioFile("audio.wav") as source:
        # Escuchar el audio y convertirlo a texto
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            print("Texto detectado:", texto)
            return texto
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
            return ""
        except sr.RequestError as e:
            print("Error al solicitar resultados de Google Speech Recognition; {0}".format(e))
            return ""

def texto_a_audio(texto):
    # Inicializar el objeto gTTS
    tts = gTTS(text=texto, lang='es')
    
    # Guardar el archivo de audio
    tts.save("audio_generado.mp3")
    
    # Reproducir el archivo de audio
    os.system("start audio_generado.mp3")

def seleccionar_fuente():
    while True:
        opcion = input("Seleccione la fuente de entrada (1 para texto, 2 para audio): ")
        if opcion == "1":
            texto = input("Ingrese el texto que desea convertir a audio: ")
            texto_a_audio(texto)
            break
        elif opcion == "2":
            texto_detectado = audio_a_texto()
            if texto_detectado:
                texto_a_audio(texto_detectado)
            break
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")

# Seleccionar fuente de entrada
seleccionar_fuente()

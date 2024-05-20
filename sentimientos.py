# Instalar las bibliotecas necesarias
#pip install sentiment-analysis-spanish
#pip install keras tensorflow

# Importar la biblioteca para el análisis de sentimientos en español
from sentiment_analysis_spanish import sentiment_analysis

# Crear una instancia del analizador de sentimientos
analizador = sentiment_analysis.SentimentAnalysisSpanish()

def interpretar_sentimiento(puntuacion):
    if puntuacion > 0.6:
        return "positivo"
    elif puntuacion < 0.4:
        return "negativo"
    else:
        return "neutral"

# Analizar el sentimiento de varios textos
textos_de_prueba = [
    "Estoy atrapado en un sueño un sueño muy raro.",       
    "No puedo olvidarla.",         
    "Este es un día triste.",         
    "El dia es muy feliz",      
    "El dia es muy asombroso.",       
    "hoy ya no tengo ganas de ir a estudiar ni por que me compre una mochila versace."     
]



for texto in textos_de_prueba:
    puntuacion = analizador.sentiment(texto)
    sentimiento = interpretar_sentimiento(puntuacion)
    print(f"Texto: '{texto}'")
    print(f"Sentimiento: {sentimiento}\n")
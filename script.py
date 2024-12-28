import pywhatkit as kit
import time
from important import MobileN

def enviar_mensaje(numero, imagen, caption, hora):
    try:
        kit.sendwhats_image(numero, imagen, caption, hora,False)
        print(f"Mensaje enviado a {numero}")
    except Exception as e:
        print(f"Error al enviar mensaje a {numero}: {str(e)}")

# Lista de números de teléfono
#MobileN = ["+5493424392941", "+5493426102045"]

imagePath = "PROMO.jpg"
Caption = "Es una prueba, no contestar"


# Iterar sobre la lista de números y enviar el mensaje
for numero in MobileN:
    enviar_mensaje(numero, imagePath, Caption, 20, 20)  # Ajusta la hora y minutos según sea necesario
    time.sleep(120)  # Pausa de 30 segundos entre cada envío
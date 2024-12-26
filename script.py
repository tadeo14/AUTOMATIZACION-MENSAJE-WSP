import pywhatkit as kit
import time

def enviar_mensaje(numero, imagen, caption, hora, minuto):
    try:
        kit.sendwhats_image(numero, imagen, caption, hora, minuto)
        print(f"Mensaje enviado a {numero}")
    except Exception as e:
        print(f"Error al enviar mensaje a {numero}: {str(e)}")

# Lista de números de teléfono
MobileN = ["+5493424392941", "+5493426102045"]

imagePath = "PROMO.jpg"
Caption = "a tumble"

# Iterar sobre la lista de números y enviar el mensaje
for numero in MobileN:
    enviar_mensaje(numero, imagePath, Caption, 10, 25)  # Ajusta la hora y minutos según sea necesario
    time.sleep(30)  # Pausa de 30 segundos entre cada envío
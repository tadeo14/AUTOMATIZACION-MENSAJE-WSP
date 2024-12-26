import pywhatkit as kit
from important import MobileN

# Enviar un mensaje directo
#kit.sendwhatmsg("+5493424392941", "Mensaje test", 10, 25)

imagePath = "PROMO.jpg" 
Caption = "a tumble"


# Iterar sobre la lista de números y enviar el mensaje
for numero in MobileN:
    kit.sendwhats_image(numero, imagePath, Caption, 20)
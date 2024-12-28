import pywhatkit as kit
import time


#Numero de la persona a enviar
phone_number = ["+5493455081206","+5493426356915","+5493424798052","+5493425114189"]

#Mensaje a enviar 
message = "Hola, esto es otra prueba"

#Archivo adjunto 

attachment = "PROMO.jpg"


#Enviamos el mensaje 
for phone_number in phone_number:

    kit.sendwhats_image(phone_number,attachment,message,15,True)
    time.sleep(10)
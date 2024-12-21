import pywhatkit as kit
import pyautogui
import time

# Enviar un mensaje directo
kit.sendwhatmsg("+5493424392941", "numero tel", "numero tel" "Mensaje test", 11, 18)

# Aumentar el tiempo de espera para que WhatsApp Web cargue correctamente
time.sleep(25)

# Ruta de la imagen que quieres enviar
image_path = r"C:\Archivos Flexxus\PROMO.jpg"

# Automáticamente carga la imagen en el chat
pyautogui.write(image_path)  # Escribe la ruta de la imagen
pyautogui.press('enter')  # Presiona Enter para cargar la imagen
time.sleep(2)  # Espera un momento para que se cargue la vista previa

# Envía la imagen
pyautogui.press('enter')  # Presiona Enter para enviar

import pyautogui
import time

# Pausa de 1 segundo entre as ações para maior segurança
pyautogui.PAUSE = 1

# Espera 5 segundos para você posicionar a janela que deseja interagir
print("Posicione a janela em 5 segundos...")
time.sleep(5)

# Move o mouse para uma posição específica (ex: 100, 200)
pyautogui.moveTo(100, 200, duration=1)

# Clica na posição atual do mouse
pyautogui.click()

# Digita um texto no campo ativo
pyautogui.write("Olá, esta é uma mensagem automatizada!", interval=0.1)

# Pressiona a tecla 'enter'
pyautogui.press('enter')

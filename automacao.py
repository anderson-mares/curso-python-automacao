import pyautogui
import os
import time

# Pausa de 1 segundo entre as ações para maior segurança
pyautogui.PAUSE = 1

# Abre o Notepad
os.system("notepad")

# Espera 2 segundos para o Notepad abrir
time.sleep(2)

# Digita o texto no Notepad
pyautogui.write("Sou a skynet e assumi o controle do seu computador!", interval=0.1)

# Arte ASCII de uma caveira
ascii_caveira = """
        ______
     .-"      "-.
    /            \\
   |              |
   |,  .-.  .-.  ,|
   | )(__/  \\__)(|
   |/     /\\     \\|
   (_     ^^     _)
    \\__|IIIIII|__/
     | \\IIIIII/ |
     \\          /
      `--------`
"""

# Digita a arte ASCII no Notepad
pyautogui.write(ascii_caveira, interval=0.05)

# Pressiona a tecla 'enter'
pyautogui.press('enter')

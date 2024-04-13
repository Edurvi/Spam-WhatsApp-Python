import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+59300000000')
sleep(10)
for i in range(25):
    pyautogui.typewrite('Mensaje de Spam')
    pyautogui.press('enter')


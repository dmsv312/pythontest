import pyautogui
from time import sleep
pyautogui.PAUSE = 1
pyautogui.hotkey('alt', 'tab')
print(pyautogui.position())
pyautogui.moveTo(954, 329, 1)
pyautogui.click()

# sleep(1)
x = pyautogui.locateOnScreen('eth.png', confidence=0.4)
sleep(3)
print(x)
pyautogui.moveTo(x.left - 200, x.top - 50, 2)
pyautogui.click()
print(pyautogui.position())
pyautogui.hotkey('alt', 'tab')


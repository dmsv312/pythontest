import pyautogui
from time import sleep
pyautogui.PAUSE = 1
pyautogui.hotkey('alt', 'tab')
print(pyautogui.position())
pyautogui.moveTo(954, 329, 1)
pyautogui.click()

# x = pyautogui.locateOnScreen('usdc.png', confidence=0.3)
# sleep(3)
# print(x)
# pyautogui.moveTo(x.left - 190, x.top - 50, 2)
pyautogui.moveTo(602, 535, 2)
pyautogui.click()
pyautogui.hotkey('alt', 'tab')


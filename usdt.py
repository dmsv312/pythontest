import pyautogui
from time import sleep
pyautogui.PAUSE = 1
pyautogui.hotkey('alt', 'tab')
# print(pyautogui.position())
pyautogui.moveTo(624, 330, 2)
pyautogui.click()
pyautogui.write('0.01')
pyautogui.moveTo(925, 484, 1)
pyautogui.click()
pyautogui.moveTo(602, 664, 1)
pyautogui.click()
# sleep(1)
# x = pyautogui.locateOnScreen('usdt.png', confidence=0.4)
# sleep(3)
# print(x)
pyautogui.moveTo(607, 605, 2)
pyautogui.click()
pyautogui.moveTo(790, 654, 1)
pyautogui.click()
sleep(3)
pyautogui.moveTo(1497, 637, 1)
pyautogui.click()
sleep(3)
x = pyautogui.locateOnScreen('example2.png', confidence=0.4)
sleep(3)
if x:
    print('success')
else:
    print('error')
    
pyautogui.hotkey('alt', 'tab')


import pyautogui
import os
from dotenv import load_dotenv
from time import sleep
pyautogui.PAUSE = 2
load_dotenv()
address = os.getenv('ADDRESS')
print(address)
# go to 2 screen
pyautogui.moveTo(1154, 10, 2)
pyautogui.click()
# open default chrome
pyautogui.moveTo(42, 15, 1)
pyautogui.click()
sleep(1)
pyautogui.moveTo(42, 148, 1)
pyautogui.click()
sleep(5)
# print site
pyautogui.moveTo(179, 87, 2)
pyautogui.click()
pyautogui.write('https://faucet.quicknode.com/drip')
pyautogui.press('enter')
# connect wallet
pyautogui.moveTo(617, 631, 2)
pyautogui.click()
# connect metamask
pyautogui.moveTo(791, 631, 2)
pyautogui.click()
# metamask next
pyautogui.moveTo(1497, 638, 2)
pyautogui.click()
# metamask connect
pyautogui.moveTo(1497, 638, 2)
pyautogui.click()
sleep(2)
# pick chain
pyautogui.moveTo(534, 704, 1)
pyautogui.click()
pyautogui.moveTo(477, 754, 1)
pyautogui.click()
# pick network
pyautogui.moveTo(722, 708, 1)
pyautogui.click()
pyautogui.moveTo(687, 791, 1)
pyautogui.click()
# click continue
pyautogui.moveTo(784, 920, 1)
pyautogui.click()
sleep(4)
# click no thanks
pyautogui.moveTo(716, 1178, 1)
pyautogui.click()
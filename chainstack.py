import pyautogui
import os
from dotenv import load_dotenv
from time import sleep
pyautogui.PAUSE = 2
load_dotenv()
address = os.getenv('ADDRESS')
apikey = os.getenv('API_KEY')
print(address)
print(apikey)
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
pyautogui.write('https://faucet.chainstack.com/holesky-testnet-faucet')
pyautogui.press('enter')
sleep(3)
# enter key
pyautogui.moveTo(617, 446, 1)
pyautogui.click()
pyautogui.write(apikey)
sleep(1)
# enter address
pyautogui.moveTo(613, 506, 1)
pyautogui.click()
pyautogui.write(address)
sleep(1)
# click claim
pyautogui.moveTo(796, 572, 1)
pyautogui.click()

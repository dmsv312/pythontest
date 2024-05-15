import pyautogui
import os
from dotenv import load_dotenv
from time import sleep
pyautogui.PAUSE = 2
load_dotenv()
address = os.getenv('ADDRESS')
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
# open new folder
pyautogui.hotkey('ctrl', 't')
sleep(1)
pyautogui.moveTo(179, 87, 2)
pyautogui.click()
pyautogui.write('https://discord.com/channels/1036357772826120242/1186301200677752872')
pyautogui.press('enter')
sleep(5)
pyautogui.click()
pyautogui.moveTo(417, 1155, 2)
pyautogui.click()
sleep(1)
pyautogui.write('GM')
pyautogui.press('enter')
sleep(1)
pyautogui.hotkey('ctrl', 'w')
sleep(1)
# close window
pyautogui.moveTo(1582, 47, 1)
pyautogui.click()
sleep(1)

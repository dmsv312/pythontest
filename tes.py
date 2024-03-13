import pyautogui
from time import sleep
import requests

pyautogui.PAUSE = 2
# pyautogui.hotkey('alt', 'tab')
print(pyautogui.position())
# # # go to 1 workspace
# pyautogui.moveTo(1228, 10, 3)
# pyautogui.click()
# # # go to 2 workspace
# pyautogui.moveTo(1263, 10, 2)
# pyautogui.click()
# # sleep(1)
# # open chrome
# pyautogui.moveTo(208, 13, 3)
# pyautogui.click()
# # print site
# pyautogui.moveTo(322, 78, 2)
# pyautogui.click()
# pyautogui.write('syncswap.xyz')
# pyautogui.press('enter')
# sleep(3)
# # change from eth to usc
# pyautogui.moveTo(795, 440, 1)
# pyautogui.click()
# # 100 
# pyautogui.moveTo(960, 400, 1)
# pyautogui.click()
# sleep(3)
# # swap
# pyautogui.moveTo(790, 654, 1)
# pyautogui.click()
# sleep(3)
# # confirm
# pyautogui.moveTo(1497, 637, 1)
# pyautogui.click()
# sleep(3)
# x = pyautogui.locateOnScreen('done.png', confidence=0.3)
# sleep(3)
# print(x)
# if x:
#     response = requests.get('http://127.0.0.1:8000/api/v1/next-transaction')
#     x = response.json()
#     new_data = {
#         "token_id_from": x["token_id_from"],
#         "token_id_to": x["token_id_to"],
#         "transaction_id": x["transaction_id"],
#     }
#     response_post = requests.post('http://127.0.0.1:8000/api/v1/save-transaction', new_data)
#     print(response_post.json())
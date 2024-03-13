import pyautogui
from time import sleep
import requests
response = requests.get('http://127.0.0.1:8000/api/v1/next-transaction')
x = response.json()
print(x)
amount = x["amount"]
pyautogui.PAUSE = 2
# pyautogui.hotkey('alt', 'tab')
# print(pyautogui.position())
sleep(1)
# # # go to 2 workspace
# pyautogui.moveTo(1263, 10, 2)
# pyautogui.click()
# open chrome
pyautogui.moveTo(208, 13, 3)
pyautogui.click()
# # print site
# pyautogui.moveTo(306, 114, 2)
# pyautogui.click()
# pyautogui.write('syncswap.xyz')
# pyautogui.press('enter')
# sleep(3)
# # go to value field and write amount from back
# pyautogui.moveTo(622, 361, 2)
# pyautogui.click()
# newamount = str(amount)
# for char in newamount:
#     pyautogui.write(char)
#     sleep(1)
# sleep(3)
# # swap
# pyautogui.moveTo(787, 680, 1)
# pyautogui.click()
# sleep(10)
# # confirm
# pyautogui.moveTo(1509, 637, 1)
# pyautogui.click()
# pyautogui.click()
# pyautogui.click()

sleep(3)
location = pyautogui.locateOnScreen('done.png', confidence=0.2)
sleep(3)
print(location)
# if location:
    
#     new_data = {
#         "token_id_from": x["token_id_from"],
#         "token_id_to": x["token_id_to"],
#         "transaction_id": x["transaction_id"],
#     }
#     response_post = requests.post('http://127.0.0.1:8000/api/v1/save-transaction', new_data)
#     print(response_post.json())

#     new_data = {
#             "transaction_id": x["transaction_id"],
#             "location": "Boy2"
#         }
#     response_post = requests.post('http://94.130.132.22/api/v1/save-transaction', new_data)
pyautogui.hotkey('alt', 'tab')
sleep(3)
# # # go to 1 workspace
# pyautogui.moveTo(1228, 10, 3)
# pyautogui.click()
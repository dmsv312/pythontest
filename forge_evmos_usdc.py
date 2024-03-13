import pyautogui
from time import sleep
import requests
import random
# response = requests.get('http://127.0.0.1:8000/api/v1/next-transaction')
# x = response.json()
# amount = x["amount"]
amount = random.randrange(10, 31, 10)
pyautogui.PAUSE = 2
sleep(1)
# open chrome
pyautogui.moveTo(208, 13, 3)
pyautogui.click()
# print site
pyautogui.moveTo(306, 114, 2)
pyautogui.click()
pyautogui.write('https://app.forge.trade/#/swap')
pyautogui.press('enter')
sleep(3)
# pick evmos
pyautogui.moveTo(1231, 401, 2)
pyautogui.click()
pyautogui.moveTo(806, 460, 1)
pyautogui.click()
# pick usdc
pyautogui.moveTo(1235, 507, 2)
pyautogui.click()
pyautogui.moveTo(656, 508, 1)
pyautogui.click()
# go to value field and write amount from back
pyautogui.moveTo(924, 399, 2)
pyautogui.click()
# enter by symbols
newamount = str(amount)
for char in newamount:
    pyautogui.write(char)
    sleep(1)
sleep(3)
# swap
pyautogui.moveTo(1084, 655, 1)
pyautogui.click()
sleep(3)
# confirm swap
pyautogui.moveTo(823, 902, 1)
pyautogui.click()
sleep(10)
# confirm in metamask
pyautogui.moveTo(1509, 637, 1)
pyautogui.click()
sleep(1)
pyautogui.click()
# check success
sleep(3)
# location = pyautogui.locateOnScreen('done.png', confidence=0.2)
# sleep(3)
# print(location)
# if location:
    
#     new_data = {
#         "token_id_from": x["token_id_from"],
#         "token_id_to": x["token_id_to"],
#         "transaction_id": x["transaction_id"]
#     }
#     response_post = requests.post('http://127.0.0.1:8000/api/v1/save-transaction', new_data)
#     print(response_post.json())

#     new_data = {
#             "transaction_id": x["transaction_id"],
#             "location": "Boy2"
#         }
#     response_post = requests.post('http://94.130.132.22/api/v1/save-transaction', new_data)

# sleep(3)
# close mozilla
pyautogui.moveTo(1587, 32, 3)
pyautogui.click()
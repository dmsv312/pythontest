import pyautogui
from time import sleep
import requests
import random
# response = requests.get('http://127.0.0.1:8000/api/v1/next-transaction')
# x = response.json()
# amount = x["amount"]
amount = random.randrange(5, 15, 1)/10
pyautogui.PAUSE = 2
sleep(1)
# open chrome
pyautogui.moveTo(208, 13, 3)
pyautogui.click()
# print site
pyautogui.moveTo(312, 115, 2)
pyautogui.click()
pyautogui.write('https://app.squidrouter.com')
sleep(1)
pyautogui.press('enter')
sleep(5)
# pick axl
pyautogui.moveTo(696, 459, 2)
pyautogui.click()
axelar = 'axe'
for char in axelar:
    pyautogui.write(char)
    sleep(1)
pyautogui.moveTo(670, 590, 1)
pyautogui.click()
sleep(7)
# pick usdc
pyautogui.moveTo(703, 649, 2)
pyautogui.click()
axelar = 'axe'
for char in axelar:
    pyautogui.write(char)
    sleep(1)
pyautogui.moveTo(670, 590, 1)
pyautogui.click()
sleep(7)
pyautogui.moveTo(867, 643, 1)
pyautogui.click()
usdc = 'axlu'
for char in usdc:
    pyautogui.write(char)
    sleep(1)
pyautogui.moveTo(656, 528, 1)
pyautogui.click()
sleep(7)
# connect wallet
pyautogui.moveTo(928, 401, 1)
pyautogui.click()
sleep(1)
pyautogui.moveTo(667, 491, 1)
pyautogui.click()
sleep(20)
# go to value field and write amount from back
pyautogui.moveTo(646, 502, 2)
pyautogui.click()
# enter by symbols
newamount = str(amount)
for char in newamount:
    pyautogui.write(char)
    sleep(1)
sleep(3)
# swap
pyautogui.moveTo(792, 930, 1)
pyautogui.click()
sleep(10)
# confirm in metamask
pyautogui.moveTo(1316, 759, 1)
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
pyautogui.moveTo(1591, 42, 3)
pyautogui.click()
sleep(1)
# go to 1 screen
pyautogui.moveTo(1125, 14, 1)
pyautogui.click()
sleep(1)
# go to 1 screen
pyautogui.moveTo(1228, 14, 1)
pyautogui.click()

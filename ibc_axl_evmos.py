import pyautogui
from time import sleep
import requests
# response = requests.get('http://127.0.0.1:8000/api/v1/next-transaction')
# x = response.json()
# amount = x["amount"]
amount = 1
pyautogui.PAUSE = 2
sleep(1)
# open chrome
pyautogui.moveTo(208, 13, 3)
pyautogui.click()
# print site
pyautogui.moveTo(306, 114, 2)
pyautogui.click()
pyautogui.write('ibc.fun')
pyautogui.press('enter')
sleep(5)

# pick evmos
pyautogui.moveTo(698, 414, 2)
pyautogui.click()
for char in 'evm':
    pyautogui.write(char)
    sleep(1)
pyautogui.moveTo(691, 466, 1)
pyautogui.click()
sleep(3)

# pick usdc
pyautogui.moveTo(698, 662, 2)
pyautogui.click()
for char in 'axe':
    pyautogui.write(char)
    sleep(1)
pyautogui.moveTo(691, 466, 1)
pyautogui.click()
sleep(3)

# connect wallet
pyautogui.moveTo(804, 841, 1)
pyautogui.click()
sleep(1)
pyautogui.moveTo(658, 386, 1)
pyautogui.click()
sleep(3)

# change sides
pyautogui.moveTo(800, 584, 1)
pyautogui.click()
sleep(3)

# go to value field and write amount from back
pyautogui.moveTo(649, 476, 2)
pyautogui.click()
# enter by symbols
newamount = str(amount)
for char in newamount:
    pyautogui.write(char)
    sleep(1)
sleep(3)
# swap
pyautogui.moveTo(797, 940, 1)
pyautogui.click()
sleep(5)
# preview route
pyautogui.moveTo(791, 941, 1)
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

# dissconnect wallet
pyautogui.moveTo(797, 940, 1)
pyautogui.click()
sleep(3)
pyautogui.moveTo(921, 339, 1)
pyautogui.click()
sleep(3)
pyautogui.moveTo(946, 397, 1)
pyautogui.click()

# close mozilla
pyautogui.moveTo(1587, 32, 3)
pyautogui.click()
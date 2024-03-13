import pyautogui
from time import sleep
import requests

pyautogui.PAUSE = 2
sleep(1)
# open chrome
pyautogui.moveTo(208, 13, 3)
pyautogui.click()
# print site
pyautogui.moveTo(306, 114, 2)
pyautogui.click()
pyautogui.write('syncswap.xyz')
pyautogui.press('enter')
sleep(3)
# change from eth to usc
pyautogui.moveTo(799, 479, 1)
pyautogui.click()
sleep(1)
# press 100 
pyautogui.moveTo(968, 457, 1)
pyautogui.click()
sleep(3)
# swap
pyautogui.moveTo(799, 704, 1)
pyautogui.click()
sleep(10)
# confirm
pyautogui.moveTo(1509, 637, 1)
pyautogui.click()
pyautogui.click()
# check success
sleep(3)
x = pyautogui.locateOnScreen('done.png', confidence=0.2)
sleep(3)
print(x)
if x:
    response = requests.get('http://127.0.0.1:8000/api/v1/next-transaction')
    x = response.json()
    new_data = {
        "token_id_from": x["token_id_from"],
        "token_id_to": x["token_id_to"],
        "transaction_id": x["transaction_id"],
    }
    response_post = requests.post('http://127.0.0.1:8000/api/v1/save-transaction', new_data)
    print(response_post.json())

    new_data = {
            "transaction_id": x["transaction_id"],
            "location": "Boy2"
        }
    response_post = requests.post('http://94.130.132.22/api/v1/save-transaction', new_data)

sleep(3)
# close mozilla
pyautogui.moveTo(1587, 32, 3)
pyautogui.click()
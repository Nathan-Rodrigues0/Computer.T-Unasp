import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")
updates = requests.get(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/getUpdates")#importando  e consultando o token ; get = pegar
print(updates["result"][-1]["message"]["chat"]["id"])#retornado somente o ID 
updates = updates.json()
updates["result"][-1]["message"]["text"]#resultado da última mensagem do telegram
#requests.post().json() / => na url: sendMessage = mandar mensagem
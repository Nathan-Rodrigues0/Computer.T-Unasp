import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")
updates = requests.get(f"https://api.telegram.or/bot('TOKEN_TELEGRAM/getUpdate')")
updates = updates.json()
updates["result"][-1]
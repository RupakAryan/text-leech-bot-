import os

API_ID    = os.environ.get("API_ID", "29978901")
API_HASH  = os.environ.get("API_HASH", "500fc876c5356cf04ed3698912dc2edf")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

import os

API_ID    = os.environ.get("API_ID", "23551823")
API_HASH  = os.environ.get("API_HASH", "36727c8db0a63181fe9963f605cc4ef4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7656304872:AAFCVqpm0bexqREh2Unk3NdtqNuAVTrXOlA") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

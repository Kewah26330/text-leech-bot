import os

API_ID    = os.environ.get("API_ID", "676580165")
API_HASH  = os.environ.get("API_HASH", "36727c8db0a63181fe9963f605cc4ef4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7951686075:AAF2IS_i-Ku8m29Z2qT7WiP_pM9OuP8URZk") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

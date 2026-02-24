import os
from dotenv import load_dotenv

load_dotenv()  # Ini akan mencari file .env di laptop


GEMINI_KEY = os.getenv("GEMINI_KEY")
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN belum di-set")

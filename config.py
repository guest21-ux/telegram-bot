import os
from dotenv import load_dotenv

load_dotenv()  # Ini akan mencari file .env di laptop


GEMINI_KEY = os.getenv("GEMINI_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN belum di-set")
if not GEMINI_KEY:
    raise RuntimeError("Gemini Key tidak terbaca")

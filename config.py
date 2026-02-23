import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN belum di-set")

GEMINI_KEY = os.getenv("GEMINI_KEY")

if not GEMINI_KEY:
    raise RuntimeError("GEMINI_KEY belum di-set")
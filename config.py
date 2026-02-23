import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:

    raise RuntimeError("TELEGRAM_TOKEN belum di-set")
GEMINI_KEY = AIzaSyAonn5GypthQQV3N3Q0HCXeGyViyRG_yMA

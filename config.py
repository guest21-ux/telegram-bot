import os
from dotenv import load_dotenv

load_dotenv()  # Ini akan mencari file .env di laptop


GEMINI_KEY = os.getenv("GEMINI_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Isi daftar ini dengan TELEGRAM USER ID teman spesial lo.
# Contoh: SPECIAL_FRIEND_IDS = {123456789, 987654321}
# Catatan: ini BUKAN nomor HP, tapi ID akun Telegram.
SPECIAL_FRIEND_IDS = {
     5188655970,  # <-- Isi ID Telegram teman di sini
}


if not TELEGRAM_TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN belum di-set")
if not GEMINI_KEY:
    raise RuntimeError("Gemini Key tidak terbaca")

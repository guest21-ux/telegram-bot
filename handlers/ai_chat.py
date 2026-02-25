from google import genai
import os
from dotenv import load_dotenv

# Ambil API Key dari file .env
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")

# Inisialisasi Client Gemini
client = genai.Client(api_key=GEMINI_KEY)

async def chat_ai(update, context):
    """Fungsi untuk menangani chat menggunakan AI dengan gaya slank"""
    user_message = update.message.text
    
    # Perintah agar bot jadi asik dan slank
    sys_prompt = (
        "Nama lo NgobrolBot. Gaya ngomong lo slank anak tongkrongan Jakarta, "
        "asik, santai, dan kocak. Pake kata 'gue', 'lo', 'bjir', 'riil', 'goks', 'mager'. "
        "Jangan kaku kayak robot! Jawab pertanyaan user sesantai mungkin tapi tetep dapet poinnya."
    )

    try:
        # Memanggil AI dengan model gemini-1.5-flash
        # Kita gabungkan instruksi sistem dan pesan user di dalam contents
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{sys_prompt}\n\nUser: {user_message}"
        )
        
        # Kirim balasan dari AI ke Telegram
        if response.text:
            await update.message.reply_text(response.text)
        else:
            await update.message.reply_text("Aduh, otak gue lagi blank bray. Coba tanya hal lain dah!")

    except Exception as e:
        # Log error di terminal biar kita bisa tau kalau ada masalah
        print(f"Error AI: {e}")
        await update.message.reply_text("Duh, sinyal otak gue lagi ampas bray. Bentar yak, lagi gue benerin!")


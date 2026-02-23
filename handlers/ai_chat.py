import google.generativeai as genai
from config import GEMINI_KEY # Pastikan sudah tambah GEMINI_KEY di config.py

# Konfigurasi Gemini
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

async def chat_ai(update, context):
    user_message = update.message.text
    
    # Instruksi Kepribadian (System Prompt)
    prompt = f"""
    Nama lo adalah PenaBot. Lo asik, santai, dan suka bercanda.
    Pake bahasa slank anak zaman sekarang (lo, gue, bjir, riil, mulyono, kecipak kecipuk, dll).
    Kalo ditanya soal sains/edukasi, jawab dengan gaya keren biar gak ngebosenin.
    Kalo user curhat, kasih tanggapan yang relate tapi tetep kocak.
    
    User bilang: {user_message}
    """

    try:
        response = model.generate_content(prompt)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("Duh, otak gue lagi nge-lag bray. Coba lagi ntar ya!")

import logging
import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Import handler buatan kita
from handlers.start import start
from handlers.help import help_cmd
from handlers.ai_chat import chat_ai



logging.basicConfig(level=logging.INFO)

def main():
    # Ambil token dari environment variable
    app = Application.builder().token(TOKEN).build()

    # Daftar perintah
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    
    # Semua chat teks bakal dijawab sama AI
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_ai))

    print("🚀 NgobrolBot Slank udah standby, bray!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()



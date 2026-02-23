import logging
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)
from handlers.ai_chat import chat_ai # Import handler baru

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("bingung", bingung))
    app.add_handler(CommandHandler("fakta", fakta))
    
    # Ganti absurd_reply dengan chat_ai
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_ai))

    print("🤖 PenaBot Slank Version is Running...")
    app.run_polling(drop_pending_updates=True)
 
        
if __name__ == "__main__":
    main()


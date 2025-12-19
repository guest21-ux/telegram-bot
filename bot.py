import logging
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from config import TOKEN
from handlers.start import start
from handlers.help import help_cmd
from handlers.absurd import absurd_reply, bingung, fakta

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("bingung", bingung))
    app.add_handler(CommandHandler("fakta", fakta))
        
    app.add_handler( 
                     MessageHandler(filters.TEXT & ~filters.COMMAND, absurd_reply)
                     )
    print("🤖 Bot berjalan...")
    app.run_polling(drop_pending_updates=True)
    
        
if __name__ == "__main__":
    main()

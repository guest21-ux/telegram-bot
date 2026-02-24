from telegram import Update
from telegram.ext import ContextTypes

async def start(update, context):
    user = update.effective_user
    await update.message.reply_text(
        f"Yo {user.first_name}! 👋\n\n"
        "Gue NgobrolBot, asisten paling gokil yang bakal nemenin hari-hari lo. "
        "Mo tanya soal sains? Curhat? Atau sekedar gabut? Gas aja, chat gue!"
    )


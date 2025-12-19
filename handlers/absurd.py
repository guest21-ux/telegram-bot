import random
from telegram import Update
from telegram.ext import ContextTypes

ABSURD_REPLIES = [
    "Aku sedang berpikir… lalu lupa mikir apa.",
    "Ini penting, tapi aku tidak tahu kenapa.",
    "Kalau kamu baca ini, berarti aku masih hidup.",
    "Aku bot, bukan cenayang.",
    "Jawaban ini tidak menjawab apa pun."
]

BINGUNG_REPLIES = [
    "Aku juga bingung, tapi kita bingung bareng.",
    "Bingung adalah tanda kamu masih waras.",
    "Coba restart hidup kamu.",
]

FAKTA_ABSURD = [
    "Fakta: Tidak semua fakta berguna.",
    "Fakta: Bot ini dibuat tanpa niat serius.",
    "Fakta: Kucing mungkin menguasai dunia."
]

async def absurd_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        random.choice(ABSURD_REPLIES)
    )

async def bingung(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        random.choice(BINGUNG_REPLIES)
    )

async def fakta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        random.choice(FAKTA_ABSURD)
    )
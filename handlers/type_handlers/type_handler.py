from telegram.ext import ContextTypes, TypeHandler
from telegram import Update


async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="TypeHandler")


type_handler = TypeHandler(Update, callback)

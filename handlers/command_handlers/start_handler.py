from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from consts import Commands


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


start_handler = CommandHandler(Commands.START.value, start)

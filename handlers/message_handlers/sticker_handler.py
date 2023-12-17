from telegram import Update
from telegram.ext import filters, ContextTypes, MessageHandler
from utils import download_file


async def download_sticker_and_echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await download_file(context.bot, update.message.sticker.file_id)
    await context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker=update.message.sticker,
        reply_to_message_id=update.message.id,
    )


sticker_handler = MessageHandler(filters.Sticker.ALL, download_sticker_and_echo)

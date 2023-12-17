from telegram import Update
from telegram.ext import filters, ContextTypes, MessageHandler


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text,
        reply_to_message_id=update.message.id,
    )


echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

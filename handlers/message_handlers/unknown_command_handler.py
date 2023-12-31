from telegram import Update
from telegram.ext import filters, ContextTypes, MessageHandler


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )


unknown_command_handler = MessageHandler(filters.COMMAND, unknown_command)

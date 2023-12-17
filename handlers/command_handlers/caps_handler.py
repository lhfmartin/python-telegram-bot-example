from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from consts import Commands


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = " ".join(context.args).upper()
    if len(text_caps) == 0:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please provide some arguments to the command",
        )
        return

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler(Commands.CAPS.value, caps)

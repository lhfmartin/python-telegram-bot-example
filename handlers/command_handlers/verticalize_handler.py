from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from consts import Commands


async def verticalize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if len(text) == 0:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please provide some arguments to the command",
        )
        return

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="\n".join(list(text))
    )


verticalize_handler = CommandHandler(Commands.VERTICALIZE.value, verticalize)

from telegram import BotCommand
from telegram.ext import Application, ApplicationBuilder

from consts import TOKEN, COMMANDS_DESCRIPTIONS


async def post_init(application: Application):
    from handlers import add_handlers

    add_handlers(application)

    commands = [
        BotCommand(x.value, COMMANDS_DESCRIPTIONS[x]) for x in COMMANDS_DESCRIPTIONS
    ]
    await application.bot.set_my_commands(commands)


application = ApplicationBuilder().token(TOKEN).post_init(post_init).build()

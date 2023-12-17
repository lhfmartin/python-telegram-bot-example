from telegram.ext import Application
from .command_handlers import command_handlers
from .inline_handlers import inline_handlers
from .message_handlers import message_handlers
from .type_handlers import type_handler


def add_handlers(application: Application):
    for handler in command_handlers + message_handlers + inline_handlers:
        application.add_handler(handler)

    application.add_handler(type_handler, -1)

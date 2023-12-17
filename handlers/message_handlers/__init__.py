from .echo_handler import echo_handler
from .unknown_command_handler import unknown_command_handler
from .sticker_handler import sticker_handler

message_handlers = (echo_handler, unknown_command_handler, sticker_handler)

from enum import Enum


class Commands(Enum):
    CAPS = "caps"
    START = "start"
    VERTICALIZE = "verticalize"


COMMANDS_DESCRIPTIONS: dict[Commands, str] = {
    Commands.START: "start the bot",
    Commands.CAPS: "shout out your message",
    Commands.VERTICALIZE: "verticalize your message",
}

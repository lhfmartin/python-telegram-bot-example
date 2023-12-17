from telegram import Bot


async def download_file(bot: Bot, file_id: str):
    await (await bot.get_file(file_id)).download_to_drive()

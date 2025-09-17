from aiogram import Bot, Dispatcher

from src.utils.config.telegram import TeleConfig
from src.bot.routers import routers
from src.database.methods import BaseMethods
from src.database.models import DBUsers

import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)

token = TeleConfig().bot_token
bot = Bot(token=token)
dp = Dispatcher()

async def start():
    await DBUsers.create_table()
    dp.include_routers(*routers)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt as e:
        logging.info("Отключение бота.")

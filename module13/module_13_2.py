from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os
from dotenv import load_dotenv
from aiogram.filters import CommandStart

config = load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


async def main():
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

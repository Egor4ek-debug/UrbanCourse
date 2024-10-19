from aiogram import Bot, Dispatcher, types
import asyncio
import os
from dotenv import load_dotenv
from aiogram.filters import CommandStart

config = load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()
bot = Bot(token=TOKEN)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message()
async def all_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

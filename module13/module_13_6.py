from aiogram.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, types
from aiogram import F
import asyncio
import os
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from dotenv import load_dotenv


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


config = load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token=TOKEN)
kb = [[KeyboardButton(text='Рассчитать')], [KeyboardButton(text='Информация')]]
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
        ]
    ]
)
keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=keyboard)


@dp.message(F.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберете опцию:', reply_markup=inline_kb)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = ("Формула Миффлина-Сан Жеора:\n"
                    "Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
                    "Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161")
    await call.message.answer(formula_text)


@dp.callback_query(F.data == 'calories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0:
            raise ValueError('Возраст должен быть положительным числом')
        await state.update_data(age=age)
        await message.answer('Введите свой рост в сантиметрах')
        await state.set_state(UserState.growth)
    except ValueError:
        await message.answer('Введите корректное число для возраста')


@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
        if growth <= 0:
            raise ValueError('Рост должен быть положительным числом')
        await state.update_data(growth=growth)
        await message.answer('Введите свой вес в килограммах')
        await state.set_state(UserState.weight)
    except ValueError:
        await message.answer('Введите корректное число для роста')


@dp.message(UserState.weight)
async def set_gender(message: types.Message, state: FSMContext):
    try:
        weight = float(message.text)
        await state.update_data(weight=weight)
        await message.answer("Введите ваш пол (м/ж):")
        await state.set_state(UserState.gender)
    except ValueError:
        await message.answer("Пожалуйста, введите корректный вес (число в кг).")


@dp.message(UserState.gender)
async def send_calories(message: types.Message, state: FSMContext):
    gender = message.text.lower()
    if gender not in ['м', 'ж']:
        await message.answer("Пожалуйста, введите 'м' для мужчины или 'ж' для женщины.")
        return

    await state.update_data(gender=gender)

    data = await state.get_data()
    age = data.get('age')
    growth = data.get('growth')
    weight = data.get('weight')
    gender = data.get('gender')

    if gender == 'м':
        bmr = 10 * weight + 6.25 * growth - 5 * age + 5  # Формула для мужчин
    else:
        bmr = 10 * weight + 6.25 * growth - 5 * age - 161  # Формула для женщин

    await message.answer(f"Ваша норма калорий: {bmr:.2f} ккал в день.")

    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

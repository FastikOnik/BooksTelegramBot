from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Привет! Я бот для управления библиотекой. "
                         "Используй команду /help для получения списка команд.")

# handlers/help.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("help"))
async def help_command(message: types.Message, state: FSMContext):
    help_text = "<b>ℹ️ Список доступных команд:</b>\n"
    help_text += "/add - Добавить новую книгу\n"
    help_text += "/list - Просмотреть список книг\n"
    help_text += "/search - Поиск книги\n"
    help_text += "/delete - Удалить книгу\n"
    await message.answer(help_text, parse_mode="HTML")

# handlers/search.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from buttons.UserKb import *

from loader import dp
from database import Database

@dp.message_handler(Command("search"))
async def search_books(message: types.Message, state: FSMContext):
    db = Database('library.db')

    search_query = message.get_args()

    if not search_query:
        await message.answer("<b>⚠️ Введите ключевое слово для поиска.</b>", parse_mode="HTML")
        return

    search_results = db.search_books(search_query)

    if not search_results:
        await message.answer("<b>❌ По вашему запросу ничего не найдено.</b>", parse_mode="HTML")
        return

    result_text = "<b>🔎 Результаты поиска:</b>\n"

    for book in search_results:
        result_text += f"<code>{book[0]}</code>. <b>📕 {book[1]}</b> - <b>📝 {book[2]}</b>\n"

    await message.answer(result_text, parse_mode="HTML", reply_markup=get_books_inline_keyboard(search_results))

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from buttons.UserKb import *

from loader import dp
from database import Database

@dp.message_handler(Command("list"))
async def list_books(message: types.Message, state: FSMContext):
    db = Database('library.db')
    books = db.get_all_books()

    if not books:
        await message.answer("В библиотеке пока нет книг.")
        return

    books_list = "<b>📋 Список книг:</b>\n"
    for book in books:
        books_list += f"<code>{book[0]}</code>.<b>📕 {book[1]}</b> - <b>📝 {book[2]}</b>\n"

    # Предложим пользователю выбрать книгу для подробной информации
    await message.answer(f"{books_list}\n<b>🧐 Выберите книгу для подробной информации:</b>",
                         reply_markup=get_books_inline_keyboard(books), parse_mode="HTML")


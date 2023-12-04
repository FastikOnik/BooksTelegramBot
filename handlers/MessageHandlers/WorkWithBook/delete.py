from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from database import Database

@dp.message_handler(Command("delete"))
async def delete_book(message: types.Message, state: FSMContext):
    db = Database('library.db')

    # Получаем идентификатор книги из сообщения пользователя
    book_id = message.get_args()

    if not book_id:
        await message.answer("<b>#️⃣ Укажите номер книги для удаления.</b>", parse_mode="HTML")
        return

    # Проверяем, существует ли книга с указанным идентификатором
    book = db.get_book_details(book_id)

    if not book:
        await message.answer("<b>🚯 Книга с указанным номером не найдена.</b>", parse_mode="HTML")
        return

    # Логика удаления книги
    db.delete_book(book_id)

    await message.answer(f"<b>Книга</b> \"<code>{book[1]}</code> - <code>{book[2]}</code>\" <b>успешно удалена!</b>", parse_mode="HTML")
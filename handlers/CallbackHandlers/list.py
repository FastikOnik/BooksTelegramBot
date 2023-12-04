from aiogram.types import CallbackQuery

from loader import dp
from database import Database

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("book_"))
async def show_book_info(callback_query: CallbackQuery):
    book_id = int(callback_query.data.split("_")[1])

    db = Database('library.db')
    book = db.get_book_details(book_id)

    if not book:
        await callback_query.message.edit_text("Книга не найдена", show_alert=True)
        return

    book_info = f"🌐 Информация о книге:\n\n" \
                f"<b>🧿 Название:</b> <code>{book[1]}</code>\n\n" \
                f"<b>✏️ Автор:</b> <code>{book[2]}</code>\n\n" \
                f"<b>ℹ️ Описание:</b> <i>{book[3]}</i>\n\n" \
                f"<b>♨️ Жанр:</b> <code>{book[4]}</code>"

    await callback_query.answer()
    await callback_query.message.edit_text(book_info, parse_mode="HTML")

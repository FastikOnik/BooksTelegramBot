from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_books_inline_keyboard(books):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for book in books:
        book_button = InlineKeyboardButton(f"{book[1]} - {book[2]}", callback_data=f"book_{book[0]}")
        keyboard.add(book_button)
    return keyboard

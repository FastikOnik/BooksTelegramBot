# handlers/add.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, state
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State

from loader import dp
from database import Database

class AddBookState(StatesGroup):
    TITLE = State()
    AUTHOR = State()
    DESCRIPTION = State()
    GENRE = State()

@dp.message_handler(Command("add"))
async def add_book_start(message: types.Message):
    # Начинаем процесс добавления новой книги
    await message.answer("<b>🆕 Введите название книги:</b>", parse_mode="HTML")
    await AddBookState.TITLE.set()

@dp.message_handler(state=AddBookState.TITLE)
async def add_book_title(message: types.Message, state: FSMContext):
    # Получаем название книги и переходим к следующему параметру
    title = message.text
    await state.update_data(title=title)

    await message.answer("<b>📝 Введите автора книги:</b>", parse_mode="HTML")
    await AddBookState.AUTHOR.set()

@dp.message_handler(state=AddBookState.AUTHOR)
async def add_book_author(message: types.Message, state: FSMContext):
    # Получаем автора книги и переходим к следующему параметру
    author = message.text
    await state.update_data(author=author)

    await message.answer("<b>ℹ️ Введите описание книги:</b>", parse_mode="HTML")
    await AddBookState.DESCRIPTION.set()

@dp.message_handler(state=AddBookState.DESCRIPTION)
async def add_book_description(message: types.Message, state: FSMContext):
    # Получаем описание книги и переходим к следующему параметру
    description = message.text
    await state.update_data(description=description)

    # Предложим выбрать жанр из списка
    genres = Database('library.db').get_all_genres()
    
    genres_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for genre in genres:
        genres_markup.add(KeyboardButton(genre))

    await message.answer("<b>♨️ Выберите жанр книги или введите свой:</b>", reply_markup=genres_markup, parse_mode="HTML")
    await AddBookState.GENRE.set()

@dp.message_handler(state=AddBookState.GENRE)
async def add_book_genre(message: types.Message, state: FSMContext):
    # Получаем жанр книги и завершаем процесс добавления
    genre = message.text
    await state.update_data(genre=genre)

    # Получаем данные из состояния
    data = await state.get_data()

    # Сохраняем книгу в базу данных
    Database('library.db').add_book(data["title"], data["author"], data["description"], data["genre"])

    await message.answer("<b>✅ Книга успешно добавлена!</b>", parse_mode="HTML")
    await state.finish()

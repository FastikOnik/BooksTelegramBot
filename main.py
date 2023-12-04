from aiogram import executor

from loader import dp
from handlers.MessageHandlers.WorkWithBook.add import *
from handlers.MessageHandlers.WorkWithBook.delete import *
from handlers.MessageHandlers.start import *
from handlers.MessageHandlers.help import *
from handlers.MessageHandlers.search import *
from handlers.MessageHandlers.list import *
from handlers.CallbackHandlers.list import *

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

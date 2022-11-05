from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


admin = 1897150814
storage = MemoryStorage()
bot = Bot('5649825386:AAHjwPRrgYv9lzfyf3xPyx1PwPmEeaaH7kQ')
headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
dp = Dispatcher(bot, storage=storage)


class FSMDistribution(StatesGroup):
    Text = State()
    

class FSMAddWell(StatesGroup):
    Code = State()
    Name = State()
    Url = State()


class FSMDelWell(StatesGroup):
    Code = State()
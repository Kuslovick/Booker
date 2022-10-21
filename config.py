from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = MemoryStorage()

admin = 1897150814
bot = Bot('TOKEN')
dp = Dispatcher(bot, storage=storage)


class FSM(StatesGroup):
    profit = State()
    expense = State()
    description = State()
    commit = State()

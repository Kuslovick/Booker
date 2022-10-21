from aiogram.dispatcher import FSMContext
from config import dp, bot, admin, FSM
from data import *
from keyboard import *


def New(dispatcher: dp):
    dispatcher.message_handler(commands=['start'])


@dp.message_handler(commands=['admin'])
async def Admin(message: types.Message):
    if message.chat.type == 'private':
        if message.chat.id == admin:
            await message.answer('Вы попали в панель администратора', reply_markup=AdminKeyboards())


@dp.callback_query_handler(text='distribution')
async def Distribution(callback: types.CallbackQuery):
    await FSM.description.set()
    await callback.message.answer('Введите текст для рассылки')


@dp.message_handler(state=FSM.description)
async def AllSend(message: types.Message, state=FSMContext):
    Users = AllUsers()
    for res in range(len(Users)):
        await bot.send_message(Users[res][0], message.text)
        await message.answer('Рассылка завершена', reply_markup=AdminKeyboards())
        await state.finish()


@dp.callback_query_handler(text='out')
async def AdminOut(callback: types.CallbackQuery):
    if callback.message.chat.id == admin:
        await callback.message.answer('Вы вышли из панели администратора', reply_markup=StartKeyboard())


@dp.message_handler(commands=['start'])
async def Start(message: types.Message):
    await message.answer(f'{UserRegister(message.chat.id)}', reply_markup=StartKeyboard())


@dp.message_handler(lambda message: message.text == 'Деньги💲')
async def Money(message: types.Message):
    await message.answer(f'Ваш баланс на данный момент:\n\n{UserMoney(message.chat.id)}', reply_markup=UserBalance())


@dp.callback_query_handler(text='profit')
async def Profit(callback: types.CallbackQuery):
    await FSM.profit.set()
    await callback.answer('Введите сумму денег что вы заработали')


@dp.message_handler(state=FSM.profit)
async def ProfitState(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        try:
            data['profit'] = int(message.text)
            UserProfit(message.chat.id, int(data['profit']))
            await message.answer('Готово')

        except ValueError:
            await message.answer('Ошибка, вы должны были ввести число')

    await state.finish()


@dp.callback_query_handler(text='expense')
async def Expense(callback: types.CallbackQuery):
    await FSM.expense.set()
    await callback.answer('Введите сумму денег что вы потратили')


@dp.message_handler(state=FSM.expense)
async def ExpenseState(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        try:
            data['expense'] = int(message.text)
            UserProfit(message.chat.id, int(data['expense']))
            await message.answer('Готово')

        except ValueError:
            await message.answer('Ошибка, вы должны были ввести число')

    await state.finish()


@dp.message_handler(lambda message: message.text == 'Прочее📁')
async def Settings(message: types.Message):
    await message.answer(f'Выберите раздел', reply_markup=UserSettings())


@dp.callback_query_handler(text='salary')
async def Salary(callback: types.CallbackQuery):
    await callback.message.answer('Введите день месяца')


@dp.callback_query_handler(text='state')
async def State(callback: types.CallbackQuery):
    await callback.message.answer(f'Ваша статистика\n\n{UserState(callback.message.chat.id)}')


@dp.message_handler(lambda message: message.text == 'Помощь👨‍💻')
async def About(message: types.Message):
    await message.answer('Помощь\n\n https://t.me/kuslovick')

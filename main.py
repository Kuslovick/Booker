from data import * 
from keyboard import *
from aiogram import executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import bot, dp, FSMDistribution, FSMAddWell, FSMDelWell, FSMContext, admin


scheduler = AsyncIOScheduler()
scheduler.add_job(PriceWellsData, 'interval', minute=30)


@dp.message_handler(commands='start')
async def Start(message: types.Message):
    RegisterData(message.chat.id)
    await message.answer('Привет, выберите раздел', reply_markup=StartKeyBoard())


@dp.message_handler(user_id=admin, commands='admin')
async def Admin(message: types.Message):
    await message.answer('Вы попали в панель админа!', reply_markup=AdminKeyBoard())


@dp.message_handler(lambda message: message.text == 'Другое🗄')
async def Other(message: types.Message):
    await message.answer('Выберите нужный раздел', reply_markup=OtherKeyBoard())


@dp.message_handler(lambda message: message.text == 'Курс Валют📈')
async def Other(message: types.Message):
    await bot.send_message(message.chat.id, f'Курс валют на данный момент\n\n{WellsData()}', disable_web_page_preview=True)


@dp.message_handler(lambda message: message.text == 'Рассылка🗣')
async def Distribution(message: types.Message):
    if message.chat.id == admin:
        await FSMDistribution.Text.set()
        await message.answer('Напишите сообщение для рассылки')


@dp.message_handler(state=FSMDistribution.Text)
async def DistributionText(message: types.Message, state: FSMContext):
    async with state.proxy():
        dist = message.text

    if dist != 'Рассылка🗣':
        for res in UsersData():
            try:
                await bot.send_message(res[0], dist)
            except:
                print(f"Ошибка отправки {res[0]}")

    else:
        await message.answer('Ошибка, повторите процедуру заново')

    await state.finish()


@dp.message_handler(lambda message: message.text == 'Добавить валюту➕')
async def NewWell(message: types.Message):
    if message.chat.id == admin:
        await FSMAddWell.Code.set()
        await message.answer('Напишите код валюты')
    

@dp.message_handler(state=FSMAddWell.Code)
async def WellCode(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['code'] = message.text

    await FSMAddWell.next()
    await message.answer('Напишите название волюты')

@dp.message_handler(state=FSMAddWell.Name)
async def WellCode(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await FSMAddWell.next()
    await message.answer('Напишите ссылку на волюту')


@dp.message_handler(state=FSMAddWell.Url)
async def WellUrl(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['url'] = message.text

    await message.answer(f"{AddWellData(data['code'], data['name'], data['url'])}")

    await state.finish()
    

@dp.message_handler(lambda message: message.text == 'Удалить валюту➖')
async def NewWell(message: types.Message):
    if message.chat.id == admin:
        await FSMDelWell.Code.set()
        await message.answer('Напишите код валюты')


@dp.message_handler(state=FSMDelWell.Code)
async def DelWellCode(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['code'] = message.text

    await message.answer(f"{DelWellData(data['code'])}")
    await state.finish()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
   
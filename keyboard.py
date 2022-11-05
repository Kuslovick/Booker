from aiogram import types


def StartKeyBoard():
    KeyBoard = \
    [
        [
            types.KeyboardButton('Курс Валют📈')
        ],
        [
            types.KeyboardButton('Другое🗄')
        ]        
    ]

    return types.ReplyKeyboardMarkup(keyboard=KeyBoard, resize_keyboard=True)


def AdminKeyBoard():
    KeyBoard = \
    [
        [
            types.KeyboardButton('Добавить валюту➕'),
            types.KeyboardButton('Удалить валюту➖')
        ],
        [
            types.KeyboardButton('Рассылка🗣')
        ],
        [
            types.KeyboardButton('Курс Валют📈')
        ]
    ]

    return types.ReplyKeyboardMarkup(keyboard=KeyBoard, resize_keyboard=True)


def OtherKeyBoard():
    KeyBoard = \
    [
        [
            types.InlineKeyboardButton('Помощь', url='https://t.me/kuslovick')
        ],
        [
            types.InlineKeyboardButton('Канал', url='https://t.me/reattery')
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=KeyBoard)



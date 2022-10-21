from aiogram import types


def StartKeyboard():
    kb = \
    [
        [
            types.KeyboardButton('Деньги💲')
        ],

        [
        types.KeyboardButton('Прочее📁'),
        types.KeyboardButton('Помощь👨‍💻')
        ]
    ]

    return types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )


def UserBalance():
    kb = \
    [
        [
            types.InlineKeyboardButton('Новая прибыль', callback_data='profit')
        ],
        [
            types.InlineKeyboardButton('Новые Затраты', callback_data='expense')
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def UserSettings():
    kb = \
    [
        [
            types.InlineKeyboardButton('Получить статистику📒', callback_data='state')
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def AdminKeyboards():
    kb = \
    [
        [
            types.InlineKeyboardButton('Рассылка сообщения', callback_data='distribution')
        ],
        [
            types.InlineKeyboardButton('Выход', callback_data='out')
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)
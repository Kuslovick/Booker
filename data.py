import sqlite3

from base.charts import connect, cursor


def UserRegister(User):
    try:
        res = cursor.execute(f'SELECT * FROM Users WHERE id = {User}').fetchone()

        if res is not None:
            return 'Вы уже добавлены в базу данных'

        else:
            cursor.execute('INSERT INTO Users VALUES (?, ?)', (User, 0))
            connect.commit()

            return 'Вы успешно добавлены в базу данных!'

    except sqlite3.ProgrammingError:
        return 'Ошибка'


def UserMoney(User):
    try:
        return cursor.execute(f'SELECT balance FROM Users WHERE id = {User}').fetchone()[0]

    except sqlite3.ProgrammingError:
        return 'Ошибка'


def UserProfit(User, Money):
    try:
        cursor.execute(f'UPDATE Users SET balance = balance + {Money} WHERE id = {User}')
        connect.commit()

    except sqlite3.ProgrammingError:
        return 'Ошибка'


def UserExpense(User, Money):
    try:
        cursor.execute(f'UPDATE Users SET balance = balance - {Money} WHERE id = {User}')
        connect.commit()

    except sqlite3.ProgrammingError:
        return 'Ошибка'


def UserState(User):
    try:
        return cursor.execute(f'SELECT * FROM User WHERE id = {User}').fetchall()[0][0]

    except sqlite3.ProgrammingError:
        return 'Ошибка'


def AllUsers():
    try:
        return cursor.execute(f'SELECT id FROM Users').fetchall()

    except sqlite3.ProgrammingError:
        print('Error')
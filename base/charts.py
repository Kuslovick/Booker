import sqlite3

connect = sqlite3.connect('base/sqlite.db', check_same_thread=False)
cursor = connect.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Articles(
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    price INT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INT NOT NULL
)''')

connect.commit()
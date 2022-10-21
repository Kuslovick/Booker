import sqlite3

connect = sqlite3.connect('base/sqlite.db')
cursor = connect.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INT NOT NULL,
    balance INT
)''')

connect.commit()
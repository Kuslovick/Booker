import requests

from base.charts import connect, cursor
from bs4 import BeautifulSoup 
from config import headers


def RegisterData(user):
    res = cursor.execute('SELECT * FROM Users WHERE id = ?', (user,)).fetchone()

    if res is not None:
        pass

    else:
        cursor.execute('INSERT INTO Users VALUES(?)', (user,))
        connect.commit() 


def UsersData():
    return cursor.execute('SELECT * FROM Users').fetchall()


def AddWellData(code, name, url):
    res = cursor.execute('SELECT * FROM Articles WHERE code = ?', (code,)).fetchone()

    try:
        if res is not None:
            return 'Эта валюта уже добавлена'

        else:
            cursor.execute('INSERT INTO Articles VALUES(?, ?, ?, ?)', (code, name, url, None,))
            connect.commit()

            PriceWellsData()

            return 'Готово'

    except:
        return 'Ошибка'


def DelWellData(code):
    res = cursor.execute('SELECT * FROM Articles WHERE code = ?', (code,)).fetchone()

    try:
        if res is not None:

            cursor.execute('DELETE FROM Articles WHERE code = ?', (code,))
            connect.commit()

            return 'Готово'

        else:
            return 'Этой валюты нет'

    except:
        return 'Ошибка'


def PriceWellsData():
    print('START')

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    
    for url in cursor.execute('SELECT url FROM Articles').fetchall():
        page = requests.get(url[0], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        well = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
            
        cursor.execute(f'UPDATE Articles SET price = ? WHERE url = ?', (str(well[0].text), url[0],) )
        connect.commit()


def WellsData():
    result = ''

    for code, name, price in cursor.execute('SELECT code, name, price FROM Articles').fetchall():
        result += f'{str(code)}   {str(name)}   {str(price)}\n\n'
    
    return result

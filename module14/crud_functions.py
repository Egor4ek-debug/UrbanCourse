import sqlite3


def initiate_db():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title STRING NOT NULL,
        description STRING,
        price INTEGER NOT NULL
        )
    ''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Products (title)')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    record = cursor.fetchall()

    connection.close()
    return record


def add_product():
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products(title,description,price) VALUES(?,?,?)',
                       (f'Продукт {i}', f'Описание {i}', i * 100))
    connection.commit()
    connection.close()

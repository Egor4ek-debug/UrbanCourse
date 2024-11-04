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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username STRING NOT NULL,
        email STRING NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

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


def add_user(username, email, age):
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,1000)',
                   (username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('telegram.db')
    cursor = connection.cursor()

    user = cursor.execute(f'SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    connection.commit()
    connection.close()
    return user is not None

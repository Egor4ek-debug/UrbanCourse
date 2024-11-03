import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username STRING NOT NULL,
    email STRING NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(10):
#     cursor.execute('INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)',
#                    (f'User{i + 1}', f'example{i + 1}@gmail.com', (i + 1) * 10, 1000))
#
# cursor.execute('''
#     UPDATE Users
#     SET balance = 500
#     WHERE id IN(
#         SELECT id FROM Users WHERE id % 2 = 1
#     )
# ''')
#
# cursor.execute('DELETE FROM Users WHERE id = 1')
#
# cursor.execute("SELECT * FROM Users ORDER BY id")
# ids = [row[0] for row in cursor.fetchall()]
#
# ids_for_delete = [id for index, id in enumerate(ids) if (index + 1) % 3 == 0]
#
# cursor.executemany("DELETE FROM Users WHERE id = ?", [(id,) for id in ids_for_delete])
#
# cursor.execute("SELECT username,email,age,balance FROM Users WHERE age != 60")
# records = cursor.fetchall()
#
# for record in records:
#     username, email, age, balance = record
#     print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
total_sum = cursor.fetchone()[0]

cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]

print(avg_balance)

connection.commit()

connection.close()

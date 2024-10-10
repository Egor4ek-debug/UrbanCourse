import requests

# Отправляем GET-запрос к JSON-данным по URL
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверяем статус код и печатаем полученные данные
if response.status_code == 200:
    data = response.json()  # Преобразуем данные в JSON
    for post in data[:5]:  # Выводим первые 5 записей
        print(f"Post ID: {post['id']}, Title: {post['title']}")
else:
    print("Error fetching data:", response.status_code)

import pandas as pd

# Считываем данные из CSV-файла
data = pd.read_csv('sample_data.csv')

# Выводим информацию о данных
print(data.info())

# Выводим основные статистические данные
print(data.describe())

# Группировка и вывод среднего значения по столбцу
grouped_data = data.groupby('Category')['Value'].mean()
print(grouped_data)


import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]

# Создание линейного графика
plt.plot(x, y, label='Data line', color='b', marker='o')

# Настройка графика
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()

# Отображение графика
plt.show()

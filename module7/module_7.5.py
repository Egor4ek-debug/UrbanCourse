import os
import time

directory = '.'
print(os.getcwd())
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        fileTime = os.path.getmtime(filepath)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(fileTime))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

def custom_write(file_name, strings):
    string_positions = {}
    with open(file_name, 'a', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            start_byte = file.tell()
            file.write(f'{str(string)}\n')
            string_positions[(line_number, start_byte)] = string
        return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

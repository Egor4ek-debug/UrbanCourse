first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
# combined_list = zip(first,second)

first_result = (len(first_length) - len(second_length) for first_length, second_length in zip(first, second) if
                len(first_length) - len(second_length) != 0)

second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))

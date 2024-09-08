first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]

second_result = [(first_string, second_string) for first_string in first_strings for second_string in second_strings if
                 len(first_string) == len(second_string)]
combined_list = first_strings + second_strings
third_result = [{name: len(name)} for name in combined_list if len(name) % 2 == 0]

print(first_result)
print(second_result)
print(third_result)
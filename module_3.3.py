def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()

print_params(a=5)

print_params(a=10, b='новая строка')

print_params(a=3.14, b='Pi', c=False)

print_params(b=25)

print_params(c=[1, 2, 3])


values_list = [1,'string',True]
values_dict = {'a':2, 'b':'new string','c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32,'Stroka']
print_params(*values_list_2,42)
my_dict = {"Roman": 2003, "Sveta": 1981}

print(f'Dict: {my_dict}')

print(f'Existing value: {my_dict.get('Roman')}')

print(f'Not existing value: {my_dict.get('Eugen')}')

my_dict.update({'Egor': 2001,
                'Dasha': 2006})
print(f'Deleted value: {my_dict.pop('Egor')}')
print(f'Modified dictionary: {my_dict}')

my_set = {1, 2, 3, 1, 1, 2, (1, 2, 3), (3, 2, 1), (1, 2, 3)}
print(f'Set: {my_set}')
my_set.update([(4, 6), 5])
my_set.discard(2)
print(f'Modified set: {my_set}')

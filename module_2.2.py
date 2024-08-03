first = int(input('Enter you first digital '))

second = int(input('Enter you second digital '))

third = int(input('Enter you third  digital '))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

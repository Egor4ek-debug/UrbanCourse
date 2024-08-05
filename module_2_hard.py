import random


def generate_password(digital):
    pairs = []

    for i in range(1, digital):
        for j in range(i + 1, digital):
            if digital % (i + j) == 0:
                pairs.append(str(i) + str(j))

    result = ''.join(pairs)
    return result


digital = random.randint(3, 20)

result = generate_password(digital)
print(f'{digital} - {result}')

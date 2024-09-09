def is_prime(func):
    def wrapper(*args, **kwargs):
        summa = func(*args, **kwargs)
        for i in range(2, summa):
            if summa % i == 0:
                print('Составное')
                return summa
        print('Простое')
        return summa

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

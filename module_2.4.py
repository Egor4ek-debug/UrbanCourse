numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []

not_primes = []

for values in numbers:
    is_prime = True
    if values == 1:
        continue
    else:
        for i in range(2, int(values**0.5)+1):
            if values % i == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(values)
    else:
        not_primes.append(values)
print(primes)
print(not_primes)

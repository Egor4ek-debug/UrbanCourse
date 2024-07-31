#1st program

print((9**0.5)*5)

#2nd program

print(9.99 > 9.98 and 1000 != 1000.1)

#3rd program

first = 1234

second = 5678
def middleDigitals(digital):
    return (digital // 10) % 100

print(middleDigitals(first) + middleDigitals(second))

#4th program

num1 = 13.42
num2 = 42.13

intPart1, fracPart1 = int(num1), num1 - int(num1)

intPart2, fracPart2 = int(num2), num2 - int(num2)

print(intPart1 == int(round(fracPart2 * 100)) or intPart2 == int(round(fracPart1 * 100)))

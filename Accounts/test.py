def plus(number1,number2):
    for _ in range(number2):
        return number1 * plus(number1)


print(plus(2,3))
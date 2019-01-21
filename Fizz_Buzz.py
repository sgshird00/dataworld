# Shird Boy


def fizz_buzz(i):
    if (i == 0):
        return i
    if (i % 3 == 0) and (i % 5 == 0):
        return "fizz_buzz"
    if (i % 3 == 0):
        return "fizz"
    if (i % 5 == 0):
        return "buzz"
    return i


print(fizz_buzz(int(input('Write a number to test: '))))

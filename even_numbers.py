c = input('enter a range for checking>>>')
b = 0
for a in range(1, int(c)):
    if (a % 2 == 0):
        print(a)
        b += 1
print(f'You have {b} even numbers in the list')

import time
f = open("test.txt", 'w', encoding='utf-8')
for i in range(5):
    f.write(f"   My sam no:{i} file    ")
    for j in range(0, 9):
        if j % 2 != 0:
            print(' '*16, end="\r")
            print(f'WrItInG'+'.'*j, end="\r")
        else:
            print(' '*16, end="\r")
            print(f'wRiTiNg'+'.'*j, end="\r")
        time.sleep(0.22)

with open("test.txt", 'r', encoding='utf-8') as f:
    print(f.read())

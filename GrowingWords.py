import time
str = input('>>please input a line in running lettes: ')
# with open("story.txt", 'r') as f:
#     str = f.readline()
ln = len(str)
print(str.lower(), end='\r')
for i in range(ln):
    # print("\r")
    print(str[0:i].upper(), end='\r')
    time.sleep(0.12)
for i in range(ln):
    # print("\r")
    print(str[0:i].lower(), end='\r')
    time.sleep(0.12)

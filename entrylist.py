i = 1
t = []


def abc():
    print('Type no for stopping entry...')
    global i
    global t
    while True:
        inp = input(f'{i}. >>>')
        if inp.lower() != 'no':
            t.append(inp)
            i += 1
            continue
        break
    print(f'length = {len(t)}  :  ', t)
    if input('Want to add more (y/Y): ').lower() == 'y':
        abc()
        return
    else:
        print('Done')


abc()
print('Success...')

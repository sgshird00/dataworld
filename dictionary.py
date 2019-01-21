
dici = {'make': 'Xiaomi', 'model': 'Redmi Y2', 'year': 2018}
print(dici)
dici["year"] = 3022
for x in dici:
    print(f'{x} : {dici[x]}')
for x, y in dici.items():
    print(x, y)
print(len(dici))
dici['colour'] = 'red'
print(dici)
del dici['year']  # or dici.pop('model')
print(dici)
dici.clear()
print(dici)
del dici
print(dici)

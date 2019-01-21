from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

toy = (date.today())
print("1 :  ", toy)
print("2 :  ", toy.day, toy.month, toy.year)
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
print("3 :  ", days[toy.weekday()])
print("4 :  ", datetime.time(datetime.now()))
print("5 :  timedelta set: ", timedelta(
    days=227, hours=11, minutes=17, seconds=99))
print('6 :  today is: ', datetime.now())
print("7 :  applying time delta: >>> ", datetime.now() +
      timedelta(days=227, hours=11, minutes=17, seconds=99))
nub = datetime.now()
print("8 :  ", nub.strftime(
    "representing string formatting:  y = %y , Y = %Y , a = %a , A = %A , b = %b , B = %B , d = %d , D = %D , c = %c , x = %x , X = %X"))
print("9 :  ", nub.strftime("%I:%M:%S %p"))
print("10:  ", nub.strftime("%H:%M"))

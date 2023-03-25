import datetime

a = datetime.datetime.today()
print(a)
b = datetime.datetime.now()
print(b)
c = datetime.date.today()
print(c)
d = datetime.datetime.today().date()
print(d)
e = datetime.datetime.today().time()
print(e)
f = datetime.datetime(2020, 2, 29, 18, 20, 50)
print(f)
print(f.strftime('%A, %d. %B %Y %I:%M%p'))

now = datetime.datetime.now()

print(now - datetime.timedelta(hours=5))
print(datetime.datetime.now() + datetime.timedelta(hours=5))
print(datetime.datetime.now() + datetime.timedelta(days=20, hours=15, minutes=8))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# enter_date = input('Please enter the date now: ')
# print(datetime.datetime.strftime(enter_date, '%Y-%m-%d %H:%M:%S'))
#
enter_date = datetime.datetime.today()
print(enter_date.now())
print(enter_date.year)
print(enter_date.month)
print(enter_date.day)
print(enter_date.hour)
print(enter_date.minute)
print(enter_date.second)
print(enter_date.microsecond)
print("Weekdays")
print(enter_date.weekday())


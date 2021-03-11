import datetime as dt

name = input('Name: ')
age = eval(input('Age: '))
year_now = dt.datetime.now().date().year
year = year_now - age + 100
print(f'Dear {name}, you will be 100 at {year}')
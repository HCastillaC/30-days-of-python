# Day 2: 30 Days of python programming

first_name = 'Hugo'
last_name = 'Castilla'
full_name = first_name + last_name
country, city, age, year, is_married, is_true, is_light_on = 'Spain', 'Caceres', 15, 2023, False, True, False

print(len(first_name))

if len(first_name) > len(last_name):
    print(f'The lenght of the first name ({len(first_name)}) is larger than the lenght of the last name({len(last_name)})')
elif len(first_name) < len(last_name):
    print(f'The lenght of the last name({len(last_name)}) is larger than the lenght of the first name ({len(first_name)})')
else:
    print(f'The lenght of the first name ({len(first_name)}) is equal to the lenght of the last name({len(last_name)})')

num1 = 5
num2 = 4
total = num1 + num2
diff = num1 - num2
product = num1 * num2
division = num1 / num2
remainder = num1 % num2
exp = num1 ** num2
floor_division = num1 // num2

radius = 30
pi = 3.14
area = (radius ** 2) * pi
circumference = 2 * radius * pi
radius = input('Write the radius: ')
radius = float(radius)
print((radius ** 2) * pi)
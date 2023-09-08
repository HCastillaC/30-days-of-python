import math as mt

#Part 1

print(f'3 + 4 = {3 + 4}')
print(f'3 - 4 = {3 - 4}')
print(f'3 * 4 = {3 * 4}')
print(f'3 / 4 = {3 / 4}')
print(f'3 ** 4 = {3 ** 4}')
print(f'4 // 3 = {4 // 3}')
print(f'4 % 3 = {4 % 3}')

print('Hugo\n', 'Who Cares\n', '(S)pain\n', 'This is the fucking second time I start this\n')


print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))

dtc = {
    1:2,
    3:4
}
print(type({3, 5}))
print(type(dtc))

#Part 2
point1 = (2, 3)
point2 = (10, 8)
print(mt.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2))
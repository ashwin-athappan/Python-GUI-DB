a = (1, 2, 3, 4, 5, 6)
print(f'The tuple is {a}')
a = list(a)
num = int(input('Enter the number to add: '))
a.append(num)
a = tuple(a)
print(f'The new tuple is {a}')
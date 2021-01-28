s = {1, 2, 3, 4, 5}
print(f'The set is {s}')
num = int(input('Enter the number of elements you want to insert: '))
for i in range(num):
    s.add(int(input(f'Enter element {i + 1}: ')))

print(f'The new set is {s}')

string = input('Enter the string to find the frequency: ')
string = string.lower()
unique_characters = set(string)

occurrence = dict()

for i in unique_characters:
    occurrence[i] = 0

for i in string:
    occurrence[i] += 1

for i in occurrence:
    print(f'{i} occurs {occurrence[i]} times')

# a = input('enter string:')
# x = set(a)
# for i in x:
#     n = 0
#     for j in a:
#         if i == j:
#             n = n + 1
#     print(i, "=", n)

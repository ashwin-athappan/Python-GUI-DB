my_list = [1, 2, 3, 4, 55]
my_new_list = []
my_sum = 0

for i in my_list:
    my_sum += i

print(f'Sum = {my_sum}, Average = {my_sum / len(my_list)}')

# my_product = 1
#
# n = int(input('Enter the length of the list:'))
# for i in range(0, n):
#     my_new_list.append(int(input()))
#
# for i in my_new_list:
#     my_product = my_product * i
#
# print(f'Product = {my_product}')

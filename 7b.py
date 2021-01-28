def list_mul(nums):
    product = 1
    for i in nums:
        product *= i

    return product


li = []
n = int(input('Enter the list size: '))
for i in range(n):
    li.append(int(input(f'Enter element {i + 1}: ')))

print(f'Product of all nums in {li} is {list_mul(li)}')

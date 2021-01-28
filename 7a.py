def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c


n1 = int(input('Enter A:'))
n2 = int(input('Enter B:'))
n3 = int(input('Enter C:'))
print(f'Maximum of 3 numbers is : {max_num(n1, n2, n3)}')

li = []
a = int(input('enter list size:'))
print('enter the words:')
for i in range(a):
    li.append(input())
m = len(li[0])
b = li[0]
for x in li:
    if len(x) > m:
        m = len(x)
        b = x

print("longest word in the list is", b, "with lenght", m)
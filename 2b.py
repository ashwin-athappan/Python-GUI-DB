a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))

median = -1

if b < a < c or c < a < b:
    median = a
elif a < b < c or c < b < a:
    median = b
elif a < c < b or b < c < a:
    median = c

print(median)

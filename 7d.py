li1 = [('Python', 90), ('C', 23), ('ADA', 90), ('Java', 47)]
print(f'Before sorting {li1}')
li1.sort(key=lambda x: x[1])
print(f'After sorting {li1}')

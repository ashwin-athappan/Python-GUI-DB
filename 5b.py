original_list = [1, 1, 2, 2, 3, 4, 5, 4, 6, 7]
new_list = []

for i in original_list:
    if i not in new_list:
        new_list.append(i)

print(f'Original List = {original_list}\nNew List = {new_list}')

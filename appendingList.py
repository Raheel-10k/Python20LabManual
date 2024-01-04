original_list = [1, 2, 3]

print(f'Original list without any append: {original_list}')

list_by_plus_operator = original_list + [4, 5, 6]
print(f'List after first append: {list_by_plus_operator}')


appendss = original_list.copy()
appendss.append(4)
appendss.append(5)
appendss.append(6)
print(f'List after second append: {appendss}')

extendedd = original_list.copy()
extendedd.extend([4, 5, 6])
print(f'List using extend: {extendedd}')
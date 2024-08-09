from functools import reduce

list1 = [1, 2, 5, 3, 6, 7, 3, 9, 2]

print(f'use sum() function :{sum(list1)}')

new_list = reduce(lambda x, y: x+y, list1)

print(f'use reduce() function :{new_list}')

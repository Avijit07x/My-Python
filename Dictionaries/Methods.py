my_dict = {'key1': 'value1',
           'key2': 'value2',
           'key3': 'value3',
           'key4': [1, 2, 3, 4, 5, 6, 7]
           }

# copy = my_dict.copy()
# print(copy)

# my_dict.clear()
print(my_dict.get('key5'))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.pop('key1')
my_dict.popitem()
my_dict['key1'] = 1

del my_dict['key2']
print(my_dict)


x = ['key1', 'key2', 'key3']
# x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
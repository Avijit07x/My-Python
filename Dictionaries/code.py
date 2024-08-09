my_dict = {'key1': 'value1',
           'key2': 'value2',
           'key3': 'value3',
           'key4': [1, 2, 3, 4, 5, 6, 7]
           }

print(my_dict.get('key5'))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict['key4'][2])


for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key}:{value}")

a = "hello"
b = "hello"

print(a is b)  # exact location of object in memory
print(a is "hello")  # exact location of object in memory
print(a == b)  # value


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]


print(list is list2) # exact location of object in memory
print(list1 == list2) # value

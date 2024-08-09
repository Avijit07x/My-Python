# Python Tuples
# Tuples are ordered collection of data items.
# They store multiple items in a single variable.
# Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable meaning we can not alter them after creation.
animals = ("cat", "dog", "bat", "mouse", "pig",
           "horse", "donkey", "goat", "cow")
print(type(animals))
print(len(animals))
print(animals[2])
print(animals[3::2])
# animals[start : end : jumpIndex]
print(animals.index("cat"))

print()
print()
print()

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)      #convert to list
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
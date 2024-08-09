#  Accepts items with the small letter “o” in the new list

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

print()
print()
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)

#  Accepts items which have more than 4 letters

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
print()

# print except 2 
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa", 2]
except2= [i for i in names if i!=2]
print(except2)

print()


list_1 = [i for i in range(10) if i != 2]
print(list_1)



names = ['A', 'B', 'C', 'D', 'E', 'F']

for name in names:
    print(name)
    
print()
# Loop over a list and print the index and value of each element
for index, name in enumerate(names):
    print(f"{index} : {name}")

print()

# Loop over a list and print the index (starting at 1) and value of each element
for index ,name in enumerate(names ,start=1):
    print(f"{index} : {name}")
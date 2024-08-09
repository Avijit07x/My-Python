# https://replit.com/@codewithharry/32-Day32-Set-Methods#.tutorial/01%20joining%20sets.md


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}

# Find the difference between set1 and set2
cities3 = cities.difference(cities2)
print(cities3)

# Remove the elements in set1 that are also present in set2

print(cities.difference(cities2))


# Find the intersection of set1 and set3

cities3 = cities.intersection(cities2)
print(cities3)

# Remove the elements from set1 that are not present in set3

cities.intersection_update(cities2)
print(cities)

# Find the symmetric difference between set1 and set3

cities3 = cities.symmetric_difference(cities2)
print(cities3)

# Update set1 with the symmetric difference of itself and set3

cities.symmetric_difference_update(cities2)
print(cities)

# Find the union of set1 and set3

cities3 = cities.union(cities2)
print(cities3)

# Update set1 with the union of itself and set3

cities.update(cities2)
print(cities)

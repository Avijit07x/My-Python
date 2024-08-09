
# Add an element to set1
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# Remove all elements from set2
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Copy set1
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.copy()
print(set3)

# Remove an element from set1
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.discard(6)

# Check if set1 and set3 are disjoint
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# Check if set1 is a subset of set3
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# Check if set1 is a superset of set3
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

# Remove a random element from set1 and return it
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# Remove the specified element from set1
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# The code is creating two sets, `cities` and `cities2`, and then using the `update()` method to add
# the elements from `cities2` to `cities`. After the update, the code prints the updated `cities` set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# The code is creating a set called `cities` with the elements "Tokyo", "Madrid", "Berlin", and
# "Delhi". Then, the `del` keyword is used to delete the `cities` set. Finally, the code tries to
# print the `cities` set, which will result in a `NameError` because the set has been deleted and no
# longer exists.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
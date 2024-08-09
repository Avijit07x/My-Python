# This code is creating a new list called `new_list` by applying a lambda function to each element in
# the original list `list1`. The lambda function squares each element. The `map()` function is used to
# apply the lambda function to each element in `list1`. Finally, the `new_list` is printed.

list1 = [1, 2, 5, 3, 6, 7, 3, 9, 2]

new_list = list(map(lambda x: x*x, list1))

print(new_list)

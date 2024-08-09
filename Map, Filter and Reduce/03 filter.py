
# This code is removing all the spaces from the string `name` and storing the result in the list
# `my_list`.
name = 'Avijit Dey'
my_list = list(filter(lambda x: x != ' ', name))
print(my_list)

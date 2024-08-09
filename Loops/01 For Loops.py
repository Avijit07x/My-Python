# 1 example
name = 'Avijit Dey'
for i in name:
    print(i, end=", ")
    if i == 'v':
        print('you are a good boy')
# 2 example
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
# 3 example
for a in range(5):  # including 0 but not 5
    print(a)
# 4 example
for x in range(6):
    print(x + 1)
# 5 example
for i in range(1, 30):
    print(i, end='\n')
    print('<><><><><><><><>')
# 6 example
for k in range(1, 15, 2):  # in general range(start, stop, step):
    print(k)

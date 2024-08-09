# reverse counting 5 to 1 using for and while loop
for i in range(5, 0, -1):
    print(i)
print()  # for new line

# while loop
count = 5
while (count > 0):
    print(count)
    # This line for step count, it can also be written like this >> count -= 1
    count = count - 1
print()  # for new line

# Else with wile loop
x = 5
while (x > 0):
    print(x)
    x = x - 1  # x -= 1
else:
    print('counter is 0')

# Number pattern using while loop
a = 1
while (a <= 5):
    for i in range(1, a+1):
        print(i,  end=" ")
    a += 1
    print()

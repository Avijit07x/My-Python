# For first pattern using while loop
i = 1
while (i <= 5):
    for j in range(1, i+1):
        print(j, end=' ')
    i = i+1
    print()
# for second pattern using for loop
for i in range(5, 0, -1):
    for j in range(1, i):
        print(j, end=' ')
    print()

for i in range(5, 0, -1):
    print(i)

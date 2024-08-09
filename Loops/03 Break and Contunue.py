#  break Statement
i = 1
while True:
    print(i)
    if (i % 51 == 0):
        break
    i += 1
print()  # For new line

# Continue Statement
for i in range(1, 11):
    if (i == 5):
        print("skip the iteration")
        continue
    print("2 *", i, "=", 2*i)

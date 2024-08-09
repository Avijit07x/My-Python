str = int(input("Enter Your Number : "))
print('Default Range Is 1 to 10')
for i in range(1, 11):  # including 1 but not 11
    ans = i * str
    print(str, '*', i, '=', ans)

str = int(input("Enter Your Number : "))
print('Default Range Is 1 to 10')
for i in range(1, 11):  # including 1 but not 11
    ans = str * i
    print(str, '*', i, '=', ans)
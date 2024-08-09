# This code is a simple calculator program that takes two numbers and an operator (+, -, *, /) as
# input from the user. It then performs the corresponding operation on the two numbers and displays
# the result.
a = int(input("Enter Your First Number : "))
b = int(input("Enter Your Second Number : "))
c = input("Enter The Operator(+ - * /) or 'q' to quit : ")

if c.lower() == 'q':
    exit()
    
ans1 = a+b
ans2 = a-b
ans3 = a*b
ans4 = a/b
if (c == "+"):
    print("Your Result Is : ", ans1)
elif (c == "-"):
    print("Your Result Is : ", ans2)
elif (c == "*"):
    print("Your Result Is : ", ans3)
elif (c == "/"):
    print("Your Result Is: ", ans4)
else:
    print(c, "Is not a valid operator")


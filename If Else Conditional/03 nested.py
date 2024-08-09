a = int(input("Enter your number :"))
if (a < 0):
    print("Number is Negetive")
elif (a > 0):
    print("Number is Positive")
    if (a <= 10):
        print("Number is Between 1-10")
    elif (a > 10 and a <= 20):  # important line
        print("Number is Between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")

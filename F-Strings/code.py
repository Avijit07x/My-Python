# The code is demonstrating the usage of f-strings and string formatting in Python.
val = 'Geeks'
print(f"{val}for {val} is a portal for {val}.")
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

price = 49.44444
print(f"For only {price:.2f} dollars!")

name = input("Enter your name : ")
age = int(input("Enter your age : "))
print(f"hello {name}!! your are {age} years old!!")

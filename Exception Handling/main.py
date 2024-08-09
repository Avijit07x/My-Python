a = input('Enter your number: ')

try:
    for i in range(1,11):
        print(f"{a} * {i} = {int(a)*i}")
except ValueError as e:
    print(e)

print('rest of the code')


# Common Exceptions in Python:

# ZeroDivisionError: Raised when attempting to divide by zero.
# TypeError: Raised when an operation is applied to an incompatible type.
# IndexError: Raised when accessing an invalid index in a sequence.
# KeyError: Raised when accessing a non-existent key in a dictionary.
# NameError: Raised when attempting to use an undefined variable.

# def sum(x, y):
#     return x+y


# print(sum(2, 4))


sum1 = lambda x,y: x+y
print(sum1(2,4))

cube = lambda x: x*x*x
# print(cube(2))

avg = lambda x, y, z: (x + y + z) / 3
print(avg(3, 5, 10))



def new (cube, value):
    """
    The function "new" takes in a function "cube" and a value, adds 10 to the result of applying the
    "cube" function to the value, and returns the final result.
    
    :param cube: A function that takes a single argument and returns the cube of that argument
    :param value: 4
    :return: The code is returning the result of calling the `new` function with the `cube` function and
    the value `4` as arguments.
    """
    return 10 + cube(value)

print(new(cube,4))

# print(appl(lambda x: x * x , 2))
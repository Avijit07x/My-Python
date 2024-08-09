def fibonacci(n):
    """
    The above function calculates the nth Fibonacci number recursively.

    :param n: The parameter `n` represents the position of the Fibonacci number you want to calculate
    :return: the nth number in the Fibonacci sequence.
    """
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


a = int(input("Enter Your Number : "))

print(fibonacci(a))

def fun():
    try:
        while True:
            user_input = int(input('Enter Your age : '))
            if user_input <= 0:
                break
            else:
                print(f'Your age is : {user_input}')
    except Exception as e:
        print(e)
    finally:
        return "This block is always executed."


x = fun()
print(x)



# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")
#   # print("I am always executed")


# x = func1()
# print(x)
# import os

# https://www.youtube.com/watch?v=Sx1Hjr67xO0

# The code `new_directory = "E:\Movies"` is assigning the path "E:\Movies" to the variable
# `new_directory`.
# new_directory = "E:\Movies"
# os.chdir(new_directory)


# The code is creating a new file named "E:\Movies\myfile.txt" in write mode ('w'). It then writes the string
# "hello my name is Avijit" to the file using the `write()` method. Finally, it closes the file using
# the `close()` method.

# important****
# If 'E:\Movies\myfile.txt' already exists, its content will be replaced with the new string.
file = open("E:\Movies\myfile.txt", 'w')
file.write("hello my name is Avijit")
file.close()


# The code is opening a file named "myfile2.txt" in read mode ('r'). It then reads the contents of the
# file using the `read()` method and assigns it to the variable `f1`. Finally, it prints the contents
# of the file and closes the file using the `close()` method.
f = open("E:\Movies\myfile.txt", 'r')
f1 = f.read()
print(f1)
f.close()


# The code is opening the file "E:\Movies\myfile.txt" in append mode ('a'). It then writes the string "\nfuck
# you." to the file using the `write()` method. This string will be added to the end of the existing
# content in the file. Finally, it closes the file using the `close()` method.
file = open("E:\Movies\myfile.txt", 'a')
file.write("\nluck you.")
file.close()

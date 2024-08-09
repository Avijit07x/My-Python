# The code is opening a file named "myfile.txt" located at "E:\Movies" in read mode. It then moves the
# file pointer to the 10th byte in the file using the `seek()` method. After that, it reads the next 5
# bytes from the file using the `read()` method and stores the data in the `data` variable. The code
# then prints the value of `data` and the current position of the file pointer using the `tell()`
# method. Finally, it closes the file using the `close()` method.

with open("E:\Movies\myfile.txt", 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)
    print(data)
    print(f.tell())
    f.close()


# The code is opening a file named "myfile4.txt" located at "E:\Movies" in write mode. It then writes
# the string "Hello World!" to the file using the `write()` method. After that, it truncates the file
# to a size of 5 bytes using the `truncate()` method.
with open("E:\Movies\myfile4.txt", 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open("E:\Movies\myfile4.txt", 'r') as f:
  print(f.read())


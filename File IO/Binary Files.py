import os

new_directory = "E:\Movies\image"
os.chdir(new_directory)


# The code is opening a file named "133.jpg" in binary mode (`'rb'`), and creating a new file named
# "133_to_new.jpg" in binary mode (`'wb'`).
img = open('133.jpg', 'rb')
img2 = open('133_to_new.jpg', 'wb')

for i in img:
    img2.write(i)

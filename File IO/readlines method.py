# This code is opening a file named "myfile.txt" located in the "E:\Movies" directory. It then reads
# the file line by line using a while loop. If there is no more line to read, the loop breaks.
# Otherwise, it prints each line to the console.
f = open("E:\Movies\myfile.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
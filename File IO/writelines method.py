# The code is opening a file named "myfile2.txt" located in the "E:\Movies" directory in write mode
# ('w'). It then writes the contents of the `lines` list to the file using the `writelines()` method.
# Each element in the `lines` list represents a line of text to be written to the file. Finally, the
# file is closed using the `close()` method.
f = open("E:\Movies\myfile2.txt", 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()


# The code is opening a file named "myfile2.txt" located in the "E:\Movies" directory in write mode
# ('w'). It then writes the contents of the `lines` list to the file using a for loop and the
# `write()` method. Each element in the `lines` list represents a line of text to be written to the
# file. Finally, the file is closed using the `close()` method.
f = open("E:\Movies\myfile3.txt", 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()
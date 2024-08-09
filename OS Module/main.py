import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# Change the working directory to a new path
new_directory = "E:\Movies"
os.chdir(new_directory)

if (not os.path.exists("Data")):
    os.mkdir("Data")

for i in range(1,101):
    os.mkdir(f"Data/Day {i}")

# rename
for i in range(1,101):
    os.rename(f"Data/Day {i}", f"Data/index.html {i}")
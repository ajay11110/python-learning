import os

# name of directory
dir_name = "/"

# list of all files 
content = os.listdir(dir_name)

# print using for loop
for item in content:
    print(item)
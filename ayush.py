# write the program to print twinkle twinkle little star in python
for i in range(1, 11):
    print("10 x", i, "=", 10 * i)

import os
#specify the directory you want to list
directory_path='/'
#list all files and directories in the specified path
content=os.listdir(directory_path)
#print each file
for item in content:
    print(item)


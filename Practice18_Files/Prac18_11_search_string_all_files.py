# 11. Write a program to search for a string in all the files of a directory.

import os
# print(os.listdir(os.getcwd()))
for file in os.listdir(os.getcwd()):
    with open(file,'r') as fr:
        for line in fr:
            data = line.find('subash')
            if data > 1:
                print(f'data:{data} is found in {file} and in line {line}')
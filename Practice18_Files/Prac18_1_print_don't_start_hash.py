# 1. Write a program to display only those lines from a file that don’t start with #.


with open("hash.txt", 'r') as f:
    for line in f:
        if not line.startswith('#'):
            print(line)

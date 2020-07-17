# 3. Write a program to display only the last 5 lines of a file.

with open('hash.txt', 'r') as f:
    count = 0
    for line in reversed(f.readlines()):
        count += 1
        if count <= 5:
            print(line)

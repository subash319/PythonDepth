# 2. Write a program to display only the first 5 lines of a file.

with open('hash.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
        if count > 5:
            break
        else:
            print(line)

# 1. Write a program that creates a list of all prime numbers from 100 to 300.

for i in range(100, 300):
    for j in range(2, i//2):
        if i % j == 0:
            break
    else:
        print(i)
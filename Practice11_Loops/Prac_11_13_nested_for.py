# 13. Write a program to print these pyramids using nested for loops.

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end='')
    print()
for i in range(1,5):
    for j in range(1,i+1):
        print(i, end='')
    print()
for i in range(1,5):
    for j in range(1,i+1):
        print(i, end='')
    print()
for i in range(10,14):
    for j in range(10,i+1):
        print(j, end=' ')
    print()
for i in range(ord('A'), ord('E')):
    for j in range(ord('A'), i+1):
        print(chr(j), end='')
    print()
for i in range(ord('A'), ord('E')):
    for j in range(ord('A'), i+1):
        print(chr(i), end='')
    print()
k = 0
for i in range(0,10):
    for j in range(ord('A')+k, ord('A')+ k +i):
        print(chr(j), end='')
        k = j+1-ord('A')
    print()
n=4
x = 'A'
for i in range(1,n+1):
   for j in range(1, i+1):
            print(x, end='')
            x = chr(ord(x)+1)
   print()
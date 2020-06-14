# 12. Write a program to print these pyramids without using nested loops.
#

for i in range(1, 5):
    print('*'*i)
for i in range(1, 5):
    print(str(i)*i)
for i in range(1, 6):
    print(chr(96+i)*i)
n=4
for i in range(1,n+1):
            print(' ' * (n-i), end='')
            print('*' * i)
n=4
for i in range(1,n+1):
  print(' ' * (n-i), end='') # for printing spaces before asterisks
  print('*' * (2*i-1))
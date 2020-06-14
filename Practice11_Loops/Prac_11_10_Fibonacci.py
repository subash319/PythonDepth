#  10. Fibonacci series is a series of numbers in which each number is the sum of previous two numbers.
#
# 1  1  2  3  5  8  13  21  34  55  89  144  233
#
#  (i) Print first n Fibonacci numbers using a for loop.
#
# (ii) Print all Fibonacci numbers less than a number n, using a while loop

n = int(input("Enter the number of Fibonacci number using a for loop"))
n0 = 1
n1 = 1
print(f"{n0} {n1}",end=' ')
for i in range(1, n+1):
    sum = n0+n1
    n0, n1 = n1, sum
    print(sum, end=" ")

num = int(input("Enter the upto which number you want to print fibonacci number"))
n0 = 1
n1 = 1
print(f"{n0} {n1}",end=' ')
sum = 0
while n0+n1 < num:
    sum = n0+n1
    n0, n1 = n1, sum
    print(sum, end=" ")
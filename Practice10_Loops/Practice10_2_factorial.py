# 2. Factorial of a non-negative integer n, is the product of all positive integers less than
# or equal to n. For example, factorial of 6 is equal to 6*5*4*3*2*1 = 720
#
#  Write a program to find out the factorial of a given number, using a while loop.

n = int(input("Enter the value of n to calculate the factorial:"))
n_only_for_display = n
fact = 1
while n:
    fact = fact * n
    n -= 1
print(f"The factorial of {n_only_for_display} is {fact}")


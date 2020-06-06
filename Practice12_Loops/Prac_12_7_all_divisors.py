# 7. Write a for loop to print all divisors of a number.
n = int(input("Enter the number to print all divisors for it:"))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end= ' ')

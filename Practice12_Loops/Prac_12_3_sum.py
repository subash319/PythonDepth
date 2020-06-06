# 3. Write a program that adds numbers entered by the user.
# Stop entering when user enters 0. Don't add numbers that are negative or greater than 500.

sum = 0
while True:
    n = int(input("Enter the number to be added to sum:"))
    if n == 0:
        break
    if 0 < n <= 500:
        sum += n
print(f'sum of all numbers entered {sum}')

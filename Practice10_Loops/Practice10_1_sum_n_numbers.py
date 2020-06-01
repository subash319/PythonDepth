#  1. Write code to find sum of first n natural numbers using a
#
# (a) while loop
#
# (b) for loop
#
# (c) without any loop

# a while loop

n = int(input("Enter the 'n' value to find sum of n natural numbers:"))
initial_n = n
sum = 0
while n:
    sum += n
    n -= 1
print(f"sum of {initial_n} natural numbers:{sum}")

n_for = initial_n
sum_for = 0
for x in range(1, n_for+1):
    sum_for += x
print(f'The sum of {initial_n} natural numbers using for loop:{sum_for}')

sum_without_loop = 0
if initial_n:
    sum_without_loop = (initial_n*(initial_n+1))/2
print(f"Sum of {initial_n} numbers without using loop is {sum_without_loop}")

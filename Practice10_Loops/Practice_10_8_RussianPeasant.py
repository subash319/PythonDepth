# 8. Write a program to multiply two numbers by Russian Peasant Method. In this method,
# any two numbers can be multiplied using only multiplication by 2, division by 2 and addition.
#
# To multiply 2 numbers, divide the first number by 2(integer division) and multiply
# the second number by 2 repeatedly till the first number reduces to 1.
#
# Suppose we have to multiply 38 and 16.
#
# 38       16
#
# 19       32
#
#   9       64
#
#   4     128
#
#   2     256
#
#   1     516
#
# Now the first number has reduced to 1 so we have stopped.
# To get the product, we will add those values on the right hand side,
# for which the corresponding left side value is odd.
#
# 38       16
#
# 19       32    <---
#
#   9       64     <---
#
#   4     128
#
#   2     256
#
#   1     512     <---
#
# On adding 32,64,512 we get 608 which is the product of 38 and 16.

num1 = first_num = int(input("Enter the first number for multplication"))
num2 = second_num = int(input("Enter the second number for multplication"))
sum = 0
while first_num >= 1:
    if first_num % 2 != 0:
        sum += second_num
        print("second_num:", second_num)
    first_num //= 2
    second_num *= 2
print(f"Prodouct of two number {num1},{num2} is:{sum}")
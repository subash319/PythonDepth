# 2. Write a function that takes a number and returns the sum of digits in it.

def sum_of_digits_in_number(num):
    sum = 0
    while num:
        sum += num%10
        num //= 10
    print("sum of the provided number is", sum)
    return sum

sum = sum_of_digits_in_number(123)
print(sum)